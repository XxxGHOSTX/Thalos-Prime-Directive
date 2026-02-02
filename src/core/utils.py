"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime™ is a proprietary system.
"""

"""
Thalos Prime Utility Functions

Common utilities including validators, Result class, and deterministic helpers.
"""

import re
import hashlib
from typing import Any, Optional, Union, List, Dict, TypeVar, Generic
from datetime import datetime
from .exceptions import ValidationError


T = TypeVar('T')


class Result(Generic[T]):
    """
    Result type for explicit success/failure handling
    
    Forces explicit error handling instead of exceptions for expected failures.
    """
    
    def __init__(self, value: Optional[T] = None, error: Optional[str] = None, 
                 success: bool = True, details: Optional[Dict] = None):
        """
        Create a Result
        
        Args:
            value: The successful value
            error: Error message if failed
            success: Whether operation succeeded
            details: Additional details
        """
        self._value = value
        self._error = error
        self._success = success
        self._details = details or {}
    
    @property
    def value(self) -> Optional[T]:
        """Get the value"""
        return self._value
    
    @property
    def error(self) -> Optional[str]:
        """Get error message"""
        return self._error
    
    @property
    def success(self) -> bool:
        """Get success status"""
        return self._success
    
    @classmethod
    def ok(cls, value: T) -> 'Result[T]':
        """Create a successful Result"""
        return cls(value=value, success=True)
    
    @classmethod
    def fail(cls, error: str, details: Optional[Dict] = None) -> 'Result[T]':
        """Create a failed Result"""
        return cls(error=error, success=False, details=details)
    
    def is_ok(self) -> bool:
        """Check if result is successful"""
        return self._success
    
    def is_err(self) -> bool:
        """Check if result is an error"""
        return not self._success
    
    def unwrap(self) -> T:
        """
        Get the value, raising exception if failed
        
        Raises:
            ValueError: If result is an error
        """
        if not self._success:
            raise ValueError(f"Called unwrap on error Result: {self._error}")
        return self._value
    
    def unwrap_or(self, default: T) -> T:
        """Get the value or return default if failed"""
        return self._value if self._success else default
    
    def expect(self, message: str) -> T:
        """
        Get the value or raise with custom message
        
        Args:
            message: Custom error message
            
        Raises:
            ValueError: If result is an error
        """
        if not self._success:
            raise ValueError(f"{message}: {self._error}")
        return self._value
    
    def details(self) -> Dict:
        """Get additional details"""
        return self._details
    
    def __repr__(self) -> str:
        if self._success:
            return f"Result.ok({self._value})"
        return f"Result.fail({self._error})"
    
    def __bool__(self) -> bool:
        """Boolean conversion returns success status"""
        return self._success


class Validator:
    """
    Collection of validation functions
    
    All validators raise ValidationError on failure.
    """
    
    @staticmethod
    def not_empty(value: str, field: str = "value") -> str:
        """Validate string is not empty"""
        if not value or not value.strip():
            raise ValidationError(
                f"{field} cannot be empty",
                field=field,
                value=value
            )
        return value.strip()
    
    @staticmethod
    def min_length(value: str, min_len: int, field: str = "value") -> str:
        """Validate minimum string length"""
        if len(value) < min_len:
            raise ValidationError(
                f"{field} must be at least {min_len} characters",
                field=field,
                value=value,
                details={'min_length': min_len, 'actual_length': len(value)}
            )
        return value
    
    @staticmethod
    def max_length(value: str, max_len: int, field: str = "value") -> str:
        """Validate maximum string length"""
        if len(value) > max_len:
            raise ValidationError(
                f"{field} must be at most {max_len} characters",
                field=field,
                value=value,
                details={'max_length': max_len, 'actual_length': len(value)}
            )
        return value
    
    @staticmethod
    def matches_pattern(value: str, pattern: str, field: str = "value") -> str:
        """Validate string matches regex pattern"""
        if not re.match(pattern, value):
            raise ValidationError(
                f"{field} does not match required pattern",
                field=field,
                value=value,
                details={'pattern': pattern}
            )
        return value
    
    @staticmethod
    def is_alpha(value: str, field: str = "value") -> str:
        """Validate string contains only letters"""
        if not value.isalpha():
            raise ValidationError(
                f"{field} must contain only letters",
                field=field,
                value=value
            )
        return value
    
    @staticmethod
    def is_alphanumeric(value: str, field: str = "value") -> str:
        """Validate string contains only letters and numbers"""
        if not value.isalnum():
            raise ValidationError(
                f"{field} must contain only letters and numbers",
                field=field,
                value=value
            )
        return value
    
    @staticmethod
    def in_range(value: Union[int, float], min_val: Union[int, float], 
                 max_val: Union[int, float], field: str = "value") -> Union[int, float]:
        """Validate numeric value is in range"""
        if not min_val <= value <= max_val:
            raise ValidationError(
                f"{field} must be between {min_val} and {max_val}",
                field=field,
                value=value,
                details={'min': min_val, 'max': max_val}
            )
        return value
    
    @staticmethod
    def is_positive(value: Union[int, float], field: str = "value") -> Union[int, float]:
        """Validate value is positive"""
        if value <= 0:
            raise ValidationError(
                f"{field} must be positive",
                field=field,
                value=value
            )
        return value
    
    @staticmethod
    def one_of(value: Any, allowed: List[Any], field: str = "value") -> Any:
        """Validate value is in allowed list"""
        if value not in allowed:
            raise ValidationError(
                f"{field} must be one of {allowed}",
                field=field,
                value=value,
                details={'allowed': allowed}
            )
        return value


def generate_id(prefix: str = "", data: Optional[str] = None) -> str:
    """
    Generate deterministic or random ID

    Args:
        prefix: Optional prefix
        data: Data to hash (if None, uses secure random token)

    Returns:
        Unique ID string
    """
    # If caller didn't provide data, use a secure random token to avoid
    # collisions caused by CPython reusing memory addresses for short-lived
    # objects (id(object())). This guarantees uniqueness for sequential
    # calls in the same process.
    if data is None:
        import secrets
        hash_hex = secrets.token_hex(8)  # 16 hex chars (8 bytes)
    else:
        hash_obj = hashlib.sha256(data.encode())
        hash_hex = hash_obj.hexdigest()[:16]

    if prefix:
        return f"{prefix}_{hash_hex}"
    return hash_hex


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename for safe filesystem use
    
    Args:
        filename: Input filename
        
    Returns:
        Sanitized filename
    """
    # Remove or replace unsafe characters
    sanitized = re.sub(r'[^\w\s\-.]', '_', filename)
    # Remove leading/trailing spaces and dots
    sanitized = sanitized.strip('. ')
    # Collapse multiple underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    return sanitized


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate string to max length
    
    Args:
        text: Input text
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated string
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def deep_merge(base: Dict, override: Dict) -> Dict:
    """
    Deep merge two dictionaries
    
    Args:
        base: Base dictionary
        override: Dictionary to merge in
        
    Returns:
        Merged dictionary
    """
    result = base.copy()
    
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    
    return result


def format_timestamp(dt: Optional[datetime] = None, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format timestamp in deterministic way
    
    Args:
        dt: Datetime to format (default: now)
        format_str: Format string
        
    Returns:
        Formatted timestamp
    """
    if dt is None:
        dt = datetime.utcnow()
    return dt.strftime(format_str)


def ensure_list(value: Any) -> List:
    """
    Ensure value is a list
    
    Args:
        value: Input value
        
    Returns:
        List containing value(s)
    """
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def safe_divide(numerator: Union[int, float], denominator: Union[int, float], 
                default: Union[int, float] = 0) -> Union[int, float]:
    """
    Safe division that returns default on division by zero
    
    Args:
        numerator: Numerator
        denominator: Denominator
        default: Default value if denominator is zero
        
    Returns:
        Division result or default
    """
    try:
        return numerator / denominator if denominator != 0 else default
    except (ZeroDivisionError, TypeError):
        return default


def clamp(value: Union[int, float], min_val: Union[int, float], 
          max_val: Union[int, float]) -> Union[int, float]:
    """
    Clamp value between min and max
    
    Args:
        value: Input value
        min_val: Minimum value
        max_val: Maximum value
        
    Returns:
        Clamped value
    """
    return max(min_val, min(value, max_val))


def validate_key(key: Any) -> bool:
    """
    Validate a storage key
    
    Valid keys must:
    - Be non-empty strings
    - Start with letter or underscore
    - Contain only letters, numbers, underscores, and hyphens
    
    Args:
        key: Key to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(key, str) or not key:
        return False
    
    # Must start with letter or underscore
    if not (key[0].isalpha() or key[0] == '_'):
        return False
    
    # Must contain only alphanumeric, underscore, or hyphen
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_-]*$'
    return bool(re.match(pattern, key))


def validate_class_name(name: Any) -> bool:
    """
    Validate a Python class name
    
    Valid class names must:
    - Be non-empty strings
    - Start with uppercase letter
    - Contain only letters and numbers
    
    Args:
        name: Class name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(name, str) or not name:
        return False
    
    # Must start with uppercase letter
    if not name[0].isupper():
        return False
    
    # Must contain only alphanumeric characters
    pattern = r'^[A-Z][a-zA-Z0-9]*$'
    return bool(re.match(pattern, name))


def validate_function_name(name: Any) -> bool:
    """
    Validate a Python function name
    
    Valid function names must:
    - Be non-empty strings
    - Start with lowercase letter or underscore
    - Contain only lowercase letters, numbers, and underscores
    
    Args:
        name: Function name to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(name, str) or not name:
        return False
    
    # Must start with lowercase letter or underscore
    if not (name[0].islower() or name[0] == '_'):
        return False
    
    # Must contain only lowercase letters, numbers, and underscores
    pattern = r'^[a-z_][a-z0-9_]*$'
    return bool(re.match(pattern, name))


def validate_identifier(identifier: Any) -> bool:
    """
    Validate a Python identifier
    
    Valid identifiers must:
    - Be non-empty strings
    - Start with letter or underscore
    - Contain only letters, numbers, and underscores
    
    Args:
        identifier: Identifier to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(identifier, str) or not identifier:
        return False
    
    # Use Python's built-in identifier validation
    return identifier.isidentifier()


def safe_get(data: Dict, *keys, default: Any = None) -> Any:
    """
    Safely access nested dictionary values
    
    Args:
        data: Dictionary to access
        *keys: Keys to traverse
        default: Default value if key not found
        
    Returns:
        Value at nested key or default
    """
    result = data
    for key in keys:
        if not isinstance(result, dict):
            return default
        result = result.get(key)
        if result is None:
            return default
    return result


def flatten_dict(nested: Dict, parent_key: str = '', sep: str = '.') -> Dict:
    """
    Flatten a nested dictionary
    
    Args:
        nested: Nested dictionary to flatten
        parent_key: Parent key for recursion
        sep: Separator for keys
        
    Returns:
        Flattened dictionary
    """
    items = []
    for k, v in nested.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def format_dict_for_display(data: Dict, indent: int = 2) -> str:
    """
    Format dictionary for display
    
    Args:
        data: Dictionary to format
        indent: Indentation level
        
    Returns:
        Formatted string
    """
    import json
    return json.dumps(data, indent=indent, default=str)


def first_or_default(items: List[T], predicate=None, default: Optional[T] = None) -> Optional[T]:
    """
    Get first item matching predicate or default
    
    Args:
        items: List of items
        predicate: Optional predicate function
        default: Default value if no match
        
    Returns:
        First matching item or default
    """
    if not items:
        return default
    
    if predicate is None:
        return items[0] if items else default
    
    for item in items:
        if predicate(item):
            return item
    
    return default


def deduplicate(items: List[T]) -> List[T]:
    """
    Remove duplicates from list while preserving order
    
    Args:
        items: List with possible duplicates
        
    Returns:
        List without duplicates
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """
    Split list into chunks
    
    Args:
        items: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
