"""Regression checks for critical web-server security controls."""
from pathlib import Path
import ast

SOURCE = Path("src/interfaces/web/immersive_server.py")


def _source_and_tree():
    text = SOURCE.read_text(encoding="utf-8")
    return text, ast.parse(text)


def test_remote_code_execution_endpoint_is_disabled():
    text, tree = _source_and_tree()
    execute = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "execute_code"
    )
    assert not any(
        isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "exec"
        for node in ast.walk(execute)
    )
    assert "Remote code execution is disabled" in text
    assert "410" in ast.unparse(execute)


def test_default_host_is_loopback_and_debug_is_false():
    text, tree = _source_and_tree()
    runs = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
        and node.func.attr == "run"
        and isinstance(node.func.value, ast.Name) and node.func.value.id == "app"
    ]
    assert runs
    call = runs[-1]
    keywords = {kw.arg: kw.value for kw in call.keywords}
    assert isinstance(keywords["debug"], ast.Constant)
    assert keywords["debug"].value is False
    assert "127.0.0.1" in ast.unparse(keywords["host"])
    assert "debug=True" not in text


def test_cors_uses_explicit_non_wildcard_allowlist():
    text, _ = _source_and_tree()
    assert "THALOS_CORS_ORIGINS" in text
    assert 'if not allowed_origins or "*" in allowed_origins' in text
    assert "CORS(app, origins=allowed_origins, supports_credentials=False)" in text


def test_memory_route_requires_strong_bearer_token():
    _, tree = _source_and_tree()
    guard = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "_admin_token_failure"
    )
    guard_text = ast.unparse(guard)
    assert "THALOS_ADMIN_TOKEN" in guard_text
    assert "compare_digest" in guard_text

def test_remote_chat_uses_safe_intent_allowlist_before_processing():
    text, tree = _source_and_tree()
    chat = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "chat"
    )
    chat_text = ast.get_source_segment(text, chat)
    assert chat_text is not None
    assert 'allowed_remote_intents = {"general", "question", "code_generation"}' in chat_text
    assert "intent = conversation.detect_intent(message)" in chat_text
    assert "if intent not in allowed_remote_intents" in chat_text
    assert "403" in chat_text
    assert chat_text.index("detect_intent") < chat_text.index("process_input")
