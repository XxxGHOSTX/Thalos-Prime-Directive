#!/usr/bin/env python3
"""
© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime is an original proprietary software system, including but not limited to
its source code, system architecture, internal logic descriptions, documentation,
interfaces, diagrams, and design materials.

Unauthorized reproduction, modification, distribution, public display, or use of
this software or its associated materials is strictly prohibited without the
express written permission of the copyright holder.

Thalos Prime™ is a proprietary system.
"""

"""
Thalos Prime v1.0 - Exception Classes

Custom exceptions for the Thalos Prime system.
Provides clear error types for different failure modes.
"""


class ThalosError(Exception):
    """Base exception for all Thalos Prime errors"""
    
    def __init__(self, message: str, code: str = "THALOS_ERROR"):
        super().__init__(message)
        self.message = message
        self.code = code
    
    def __str__(self):
        return f"[{self.code}] {self.message}"


class CISError(ThalosError):
    """Errors related to the Central Intelligence System"""
    
    def __init__(self, message: str):
        super().__init__(message, "CIS_ERROR")


class CISNotBootedError(CISError):
    """Raised when attempting operations before CIS boot"""
    
    def __init__(self, operation: str = "operation"):
        super().__init__(f"Cannot perform {operation} - CIS not booted")
        self.code = "CIS_NOT_BOOTED"


class CISAlreadyBootedError(CISError):
    """Raised when attempting to boot an already booted CIS"""
    
    def __init__(self):
        super().__init__("CIS is already booted")
        self.code = "CIS_ALREADY_BOOTED"


class SubsystemError(ThalosError):
    """Errors related to subsystem operations"""
    
    def __init__(self, subsystem: str, message: str):
        super().__init__(f"{subsystem}: {message}", "SUBSYSTEM_ERROR")
        self.subsystem = subsystem


class MemoryError(SubsystemError):
    """Errors related to the Memory subsystem"""
    
    def __init__(self, message: str):
        super().__init__("Memory", message)
        self.code = "MEMORY_ERROR"


class KeyExistsError(MemoryError):
    """Raised when attempting to create a key that already exists"""
    
    def __init__(self, key: str):
        super().__init__(f"Key already exists: {key}")
        self.key = key
        self.code = "KEY_EXISTS"


class KeyNotFoundError(MemoryError):
    """Raised when a required key is not found"""
    
    def __init__(self, key: str):
        super().__init__(f"Key not found: {key}")
        self.key = key
        self.code = "KEY_NOT_FOUND"


class CodeGenError(SubsystemError):
    """Errors related to the Code Generator subsystem"""
    
    def __init__(self, message: str):
        super().__init__("CodeGen", message)
        self.code = "CODEGEN_ERROR"


class TemplateNotFoundError(CodeGenError):
    """Raised when a requested template is not found"""
    
    def __init__(self, template_name: str):
        super().__init__(f"Template not found: {template_name}")
        self.template_name = template_name
        self.code = "TEMPLATE_NOT_FOUND"


class TemplateExistsError(CodeGenError):
    """Raised when attempting to register a template that already exists"""
    
    def __init__(self, template_name: str):
        super().__init__(f"Template already exists: {template_name}")
        self.template_name = template_name
        self.code = "TEMPLATE_EXISTS"


class GenerationError(CodeGenError):
    """Raised when code generation fails"""
    
    def __init__(self, reason: str):
        super().__init__(f"Code generation failed: {reason}")
        self.code = "GENERATION_FAILED"


class InterfaceError(ThalosError):
    """Errors related to interface operations"""
    
    def __init__(self, interface: str, message: str):
        super().__init__(f"{interface}: {message}", "INTERFACE_ERROR")
        self.interface = interface


class CLIError(InterfaceError):
    """Errors related to the CLI interface"""
    
    def __init__(self, message: str):
        super().__init__("CLI", message)
        self.code = "CLI_ERROR"


class APIError(InterfaceError):
    """Errors related to the API interface"""
    
    def __init__(self, message: str, status_code: int = 500):
        super().__init__("API", message)
        self.code = "API_ERROR"
        self.status_code = status_code


class ValidationError(ThalosError):
    """Errors related to input validation"""
    
    def __init__(self, field: str, reason: str):
        super().__init__(f"Validation failed for '{field}': {reason}", "VALIDATION_ERROR")
        self.field = field
        self.reason = reason


class ConfigurationError(ThalosError):
    """Errors related to system configuration"""
    
    def __init__(self, message: str):
        super().__init__(message, "CONFIG_ERROR")
