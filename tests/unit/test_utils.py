"""
Thalos Prime v1.0 - Unit Tests for Core Utilities

Tests for logging, configuration, exceptions, and utility functions
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.utils import (
    validate_key, validate_class_name, validate_function_name,
    validate_identifier, safe_get, flatten_dict, truncate_string,
    format_dict_for_display, ensure_list, first_or_default,
    deduplicate, chunk_list, Result
)
from core.config import ThalosConfig
from core.exceptions import (
    ThalosError, CISError, CISNotBootedError, KeyExistsError,
    KeyNotFoundError, ValidationError
)


def test_validate_key():
    """Test key validation"""
    # Valid keys
    assert validate_key('mykey') is True
    assert validate_key('my_key') is True
    assert validate_key('my-key') is True
    assert validate_key('key123') is True
    assert validate_key('_private') is True
    
    # Invalid keys
    assert validate_key('') is False
    assert validate_key('123key') is False  # Starts with number
    assert validate_key('my key') is False  # Contains space
    assert validate_key('key.name') is False  # Contains dot
    assert validate_key(None) is False
    
    print("✓ Key validation test passed")


def test_validate_class_name():
    """Test class name validation"""
    # Valid class names
    assert validate_class_name('MyClass') is True
    assert validate_class_name('User') is True
    assert validate_class_name('MyClass123') is True
    assert validate_class_name('A') is True
    
    # Invalid class names
    assert validate_class_name('myclass') is False  # Lowercase start
    assert validate_class_name('123Class') is False  # Starts with number
    assert validate_class_name('My Class') is False  # Contains space
    assert validate_class_name('') is False
    
    print("✓ Class name validation test passed")


def test_validate_function_name():
    """Test function name validation"""
    # Valid function names
    assert validate_function_name('my_function') is True
    assert validate_function_name('process') is True
    assert validate_function_name('_private') is True
    assert validate_function_name('func123') is True
    
    # Invalid function names
    assert validate_function_name('MyFunction') is False  # Uppercase start
    assert validate_function_name('123func') is False  # Starts with number
    assert validate_function_name('my-func') is False  # Contains hyphen
    
    print("✓ Function name validation test passed")


def test_validate_identifier():
    """Test identifier validation"""
    # Valid identifiers
    assert validate_identifier('variable') is True
    assert validate_identifier('_private') is True
    assert validate_identifier('Capitalized') is True
    assert validate_identifier('var123') is True
    
    # Invalid identifiers
    assert validate_identifier('123var') is False
    assert validate_identifier('my-var') is False
    assert validate_identifier('my var') is False
    
    print("✓ Identifier validation test passed")


def test_safe_get():
    """Test safe dictionary access"""
    data = {
        'level1': {
            'level2': {
                'value': 'found'
            }
        }
    }
    
    # Successful access
    assert safe_get(data, 'level1', 'level2', 'value') == 'found'
    assert safe_get(data, 'level1', 'level2') == {'value': 'found'}
    
    # Missing keys
    assert safe_get(data, 'missing') is None
    assert safe_get(data, 'level1', 'missing', default='default') == 'default'
    
    print("✓ Safe get test passed")


def test_flatten_dict():
    """Test dictionary flattening"""
    nested = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
            }
        }
    }
    
    flat = flatten_dict(nested)
    assert flat['a'] == 1
    assert flat['b.c'] == 2
    assert flat['b.d.e'] == 3
    
    print("✓ Flatten dict test passed")


def test_truncate_string():
    """Test string truncation"""
    long_string = "This is a very long string that should be truncated"
    
    # Truncation needed
    result = truncate_string(long_string, 20)
    assert len(result) == 20
    assert result.endswith('...')
    
    # No truncation needed
    short_string = "short"
    assert truncate_string(short_string, 20) == "short"
    
    print("✓ Truncate string test passed")


def test_ensure_list():
    """Test ensure_list utility"""
    assert ensure_list(None) == []
    assert ensure_list([1, 2, 3]) == [1, 2, 3]
    assert ensure_list('single') == ['single']
    assert ensure_list(42) == [42]
    
    print("✓ Ensure list test passed")


def test_first_or_default():
    """Test first_or_default utility"""
    items = [1, 2, 3, 4, 5]
    
    # Without predicate
    assert first_or_default(items) == 1
    assert first_or_default([]) is None
    assert first_or_default([], default=0) == 0
    
    # With predicate
    assert first_or_default(items, lambda x: x > 3) == 4
    assert first_or_default(items, lambda x: x > 10) is None
    
    print("✓ First or default test passed")


def test_deduplicate():
    """Test list deduplication"""
    items = [1, 2, 2, 3, 1, 4, 3, 5]
    result = deduplicate(items)
    
    assert result == [1, 2, 3, 4, 5]
    assert len(result) == 5
    
    print("✓ Deduplicate test passed")


def test_chunk_list():
    """Test list chunking"""
    items = [1, 2, 3, 4, 5, 6, 7]
    
    chunks = chunk_list(items, 3)
    assert chunks == [[1, 2, 3], [4, 5, 6], [7]]
    
    chunks = chunk_list(items, 2)
    assert len(chunks) == 4
    
    print("✓ Chunk list test passed")


def test_result_class():
    """Test Result class"""
    # Success result
    success = Result.ok("value")
    assert success.success is True
    assert success.value == "value"
    assert success.error is None
    assert bool(success) is True
    
    # Failure result
    failure = Result.fail("error message")
    assert failure.success is False
    assert failure.error == "error message"
    assert bool(failure) is False
    
    print("✓ Result class test passed")


def test_config_defaults():
    """Test configuration with defaults"""
    config = ThalosConfig()
    
    # Check defaults are applied
    assert config.get('system', 'version') == '1.0'
    assert config.get('system', 'name') == 'ThalosPrime'
    assert config.get_bool('cis', 'enabled') is True
    assert config.get_bool('codegen', 'deterministic') is True
    
    print("✓ Config defaults test passed")


def test_config_set_and_get():
    """Test configuration set and get"""
    config = ThalosConfig()
    
    config.set('custom', 'key', 'value')
    assert config.get('custom', 'key') == 'value'
    
    config.set('system', 'custom_key', '123')
    assert config.get_int('system', 'custom_key') == 123
    
    print("✓ Config set and get test passed")


def test_config_section():
    """Test getting configuration section"""
    config = ThalosConfig()
    
    system_config = config.get_section('system')
    assert 'version' in system_config
    assert 'name' in system_config
    
    print("✓ Config section test passed")


def test_config_to_dict():
    """Test configuration export"""
    config = ThalosConfig()
    
    exported = config.to_dict()
    assert 'system' in exported
    assert 'cis' in exported
    assert 'memory' in exported
    
    print("✓ Config to dict test passed")


def test_exception_hierarchy():
    """Test exception class hierarchy"""
    # Base exception
    base_error = ThalosError("base message")
    assert str(base_error) == "[THALOS_ERROR] base message"
    
    # CIS exceptions
    cis_error = CISError("CIS issue")
    assert "CIS_ERROR" in str(cis_error)
    
    not_booted = CISNotBootedError("test_operation")
    assert "not booted" in str(not_booted).lower()
    
    print("✓ Exception hierarchy test passed")


def test_memory_exceptions():
    """Test memory-specific exceptions"""
    key_exists = KeyExistsError("mykey")
    assert key_exists.key == "mykey"
    assert "KEY_EXISTS" in str(key_exists) or "already exists" in str(key_exists).lower()
    
    key_not_found = KeyNotFoundError("missing")
    assert key_not_found.key == "missing"
    
    print("✓ Memory exceptions test passed")


def test_validation_exception():
    """Test validation exception"""
    validation_error = ValidationError("username", "must be at least 3 characters")
    assert validation_error.field == "username"
    assert validation_error.reason == "must be at least 3 characters"
    
    print("✓ Validation exception test passed")


if __name__ == '__main__':
    print("Running Core Utilities Unit Tests...")
    test_validate_key()
    test_validate_class_name()
    test_validate_function_name()
    test_validate_identifier()
    test_safe_get()
    test_flatten_dict()
    test_truncate_string()
    test_ensure_list()
    test_first_or_default()
    test_deduplicate()
    test_chunk_list()
    test_result_class()
    test_config_defaults()
    test_config_set_and_get()
    test_config_section()
    test_config_to_dict()
    test_exception_hierarchy()
    test_memory_exceptions()
    test_validation_exception()
    print("\nAll Core Utilities tests passed!")
