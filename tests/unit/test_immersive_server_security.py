"""Static security regression tests for the immersive HTTP server."""

import ast
from pathlib import Path


SERVER = (
    Path(__file__).resolve().parents[2]
    / "src"
    / "interfaces"
    / "web"
    / "immersive_server.py"
)


def _source_and_tree():
    source = SERVER.read_text(encoding="utf-8")
    return source, ast.parse(source)


def test_no_remote_code_execution_or_memory_dump_routes():
    source, tree = _source_and_tree()
    routes = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute):
                    if isinstance(decorator.func.value, ast.Name) and decorator.func.value.id == "app":
                        if decorator.func.attr == "route" and decorator.args:
                            arg = decorator.args[0]
                            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                                routes.add(arg.value)

    assert "/api/execute" not in routes
    assert "/api/memory" not in routes
    assert "exec(" not in source


def test_chat_endpoint_is_explicitly_disabled():
    _, tree = _source_and_tree()
    chat_functions = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "chat_disabled"
    ]
    assert len(chat_functions) == 1
    assert any(
        isinstance(node, ast.Constant) and node.value == 503
        for node in ast.walk(chat_functions[0])
    )


def test_server_is_loopback_only_and_debug_is_disabled():
    _, tree = _source_and_tree()
    app_run_calls = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "app"
        and node.func.attr == "run"
    ]
    assert len(app_run_calls) == 1
    kwargs = {kw.arg: kw.value for kw in app_run_calls[0].keywords}
    assert isinstance(kwargs.get("host"), ast.Constant)
    assert kwargs["host"].value == "127.0.0.1"
    assert isinstance(kwargs.get("debug"), ast.Constant)
    assert kwargs["debug"].value is False


if __name__ == "__main__":
    test_no_remote_code_execution_or_memory_dump_routes()
    test_chat_endpoint_is_explicitly_disabled()
    test_server_is_loopback_only_and_debug_is_disabled()
    print("Immersive server security regression tests passed.")
