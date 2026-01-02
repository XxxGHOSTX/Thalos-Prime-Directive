"""
Thalos Prime v1.0 - Main Package
"""

from .core import CIS, MemoryModule
from .interfaces import CLI, API
from .codegen import CodeGenerator

__version__ = '1.0'

__all__ = ['CIS', 'MemoryModule', 'CLI', 'API', 'CodeGenerator']
