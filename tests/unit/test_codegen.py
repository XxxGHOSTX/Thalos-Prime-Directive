"""
Thalos Prime v1.0 - Unit Tests for Code Generator

Tests for deterministic code generation with pure functions
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from codegen import CodeGenerator


def test_codegen_initialization():
    """Test Code Generator initialization"""
    codegen = CodeGenerator()
    assert codegen is not None
    assert len(codegen.list_templates()) == 0
    assert codegen.track_history is False
    print("✓ Code Generator initialization test passed")


def test_codegen_with_history():
    """Test Code Generator with history tracking"""
    codegen = CodeGenerator(track_history=True)
    assert codegen.track_history is True
    assert len(codegen.get_history()) == 0
    print("✓ Code Generator with history test passed")


def test_template_registration():
    """Test template registration"""
    codegen = CodeGenerator()
    
    template = "Hello {name}!"
    result = codegen.register_template('greeting', template)
    assert result is True
    assert 'greeting' in codegen.list_templates()
    
    # Test duplicate registration fails
    result = codegen.register_template('greeting', template)
    assert result is False
    
    print("✓ Template registration test passed")


def test_code_generation():
    """Test deterministic code generation from template"""
    codegen = CodeGenerator()
    
    template = "class {class_name}:\n    pass"
    codegen.register_template('class', template)
    
    # Generate code
    code = codegen.generate('class', {'class_name': 'MyClass'})
    assert code is not None
    assert 'class MyClass:' in code
    
    # Test with non-existent template
    code = codegen.generate('nonexistent', {})
    assert code is None
    
    # Test with missing context
    code = codegen.generate('class', {})
    assert code is None
    
    print("✓ Code generation test passed")


def test_class_generation():
    """Test automatic class generation"""
    codegen = CodeGenerator()
    
    # Generate class with default methods (includes __init__)
    code = codegen.generate_class('TestModule')
    assert 'class TestModule:' in code
    assert 'def __init__(self)' in code
    
    # Generate class with custom methods (including __init__)
    code = codegen.generate_class('TestModule', ['__init__', 'process', 'validate'])
    assert 'class TestModule:' in code
    assert 'def __init__(self)' in code
    assert 'def process(self):' in code
    assert 'def validate(self):' in code
    
    print("✓ Class generation test passed")


def test_function_generation():
    """Test automatic function generation"""
    codegen = CodeGenerator()
    
    # Generate function without parameters
    code = codegen.generate_function('test_function')
    assert 'def test_function():' in code
    
    # Generate function with parameters
    code = codegen.generate_function('process_data', ['input', 'options'])
    assert 'def process_data(input, options):' in code
    
    print("✓ Function generation test passed")


def test_deterministic_output():
    """Test that generation produces deterministic output"""
    codegen1 = CodeGenerator()
    codegen2 = CodeGenerator()
    
    # Register same template in both
    template = "Result: {value}"
    codegen1.register_template('test', template)
    codegen2.register_template('test', template)
    
    # Generate with same context
    context = {'value': '123'}
    code1 = codegen1.generate('test', context)
    code2 = codegen2.generate('test', context)
    
    # Output should be identical
    assert code1 == code2
    
    # Generate class with same inputs
    class_code1 = codegen1.generate_class('MyClass', ['method1', 'method2'])
    class_code2 = codegen2.generate_class('MyClass', ['method1', 'method2'])
    assert class_code1 == class_code2
    
    print("✓ Deterministic output test passed")


def test_generation_history():
    """Test generation history tracking"""
    codegen = CodeGenerator(track_history=True)
    
    codegen.register_template('test', "Test {value}")
    codegen.generate('test', {'value': '123'})
    
    history = codegen.get_history()
    assert len(history) == 1
    assert history[0]['template'] == 'test'
    assert history[0]['context_keys'] == ['value']
    
    codegen.clear_history()
    assert len(codegen.get_history()) == 0
    
    print("✓ Generation history test passed")


def test_stateless_operation():
    """Test that generator is stateless (except optional history)"""
    codegen = CodeGenerator()
    
    # Multiple generations should not affect each other
    codegen.register_template('t1', "Output: {x}")
    codegen.register_template('t2', "Result: {y}")
    
    code1 = codegen.generate('t1', {'x': 'A'})
    code2 = codegen.generate('t2', {'y': 'B'})
    code3 = codegen.generate('t1', {'x': 'C'})
    
    # Each should be independent
    assert 'Output: A' in code1
    assert 'Result: B' in code2
    assert 'Output: C' in code3
    
    print("✓ Stateless operation test passed")


def test_list_templates_sorted():
    """Test that template listing is sorted (for determinism)"""
    codegen = CodeGenerator()
    
    codegen.register_template('zeta', 'z')
    codegen.register_template('alpha', 'a')
    codegen.register_template('beta', 'b')
    
    templates = codegen.list_templates()
    assert templates == ['alpha', 'beta', 'zeta']
    
    print("✓ List templates sorted test passed")


def test_isolation_from_cis():
    """Test that CodeGen works independently without CIS"""
    # This test verifies CodeGen can operate in isolation
    codegen = CodeGenerator()
    
    # Should work without any external dependencies
    code = codegen.generate_class('Standalone', ['run'])
    assert code is not None
    assert 'class Standalone:' in code
    assert 'def run(self):' in code
    
    # Should work with templates
    codegen.register_template('simple', 'Value: {v}')
    code = codegen.generate('simple', {'v': 'test'})
    assert code == 'Value: test'
    
    print("✓ Isolation from CIS test passed")


if __name__ == '__main__':
    print("Running Code Generator Unit Tests...")
    test_codegen_initialization()
    test_codegen_with_history()
    test_template_registration()
    test_code_generation()
    test_class_generation()
    test_function_generation()
    test_deterministic_output()
    test_generation_history()
    test_stateless_operation()
    test_list_templates_sorted()
    test_isolation_from_cis()
    print("\nAll Code Generator tests passed!")
