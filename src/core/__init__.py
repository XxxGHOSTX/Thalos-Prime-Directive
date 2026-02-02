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
Thalos Prime v1.0 - Core Systems Module

Core components:
- CIS: Central Intelligence System (orchestrator)
- MemoryModule: In-memory key-value storage
- ThalosConfig: Configuration management
- ThalosLogger: Logging utilities
- Exceptions: Custom exception classes
"""

from .cis import CIS
from .memory import MemoryModule
from .config import ThalosConfig, load_config
from .logging import ThalosLogger, get_logger
from .exceptions import (
    ThalosError,
    CISError,
    CISNotBootedError,
    CISAlreadyBootedError,
    SubsystemError,
    MemoryError,
    KeyExistsError,
    KeyNotFoundError,
    CodeGenError,
    TemplateNotFoundError,
    TemplateExistsError,
    GenerationError,
    InterfaceError,
    CLIError,
    APIError,
    ValidationError,
    ConfigurationError
)

__all__ = [
    'CIS',
    'MemoryModule',
    'ThalosConfig',
    'load_config',
    'ThalosLogger',
    'get_logger',
    'ThalosError',
    'CISError',
    'CISNotBootedError',
    'CISAlreadyBootedError',
    'SubsystemError',
    'MemoryError',
    'KeyExistsError',
    'KeyNotFoundError',
    'CodeGenError',
    'TemplateNotFoundError',
    'TemplateExistsError',
    'GenerationError',
    'InterfaceError',
    'CLIError',
    'APIError',
    'ValidationError',
    'ConfigurationError'
]
