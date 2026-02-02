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
Thalos Prime v1.0 - Logging Module

Provides configurable logging for the Thalos Prime system.
Maintains deterministic behavior by allowing log level configuration.
"""

import logging
import sys
from typing import Optional

# Default log format
DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ThalosLogger:
    """
    Centralized logging for Thalos Prime
    
    Provides:
    - Configurable log levels
    - Console and file output
    - Consistent formatting
    """
    
    _instance: Optional['ThalosLogger'] = None
    _initialized: bool = False
    
    def __new__(cls):
        """Singleton pattern for consistent logging across the system"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the logger (only once)"""
        if ThalosLogger._initialized:
            return
            
        self.logger = logging.getLogger('thalos')
        self.logger.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(
            logging.Formatter(DEFAULT_FORMAT, DEFAULT_DATE_FORMAT)
        )
        self.logger.addHandler(console_handler)
        
        ThalosLogger._initialized = True
    
    def set_level(self, level: str) -> None:
        """
        Set the logging level
        
        Args:
            level: One of 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        """
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.logger.setLevel(level_map.get(level.upper(), logging.INFO))
    
    def add_file_handler(self, filepath: str, level: str = 'DEBUG') -> None:
        """
        Add file logging
        
        Args:
            filepath: Path to log file
            level: Minimum log level for file
        """
        file_handler = logging.FileHandler(filepath)
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        file_handler.setLevel(level_map.get(level.upper(), logging.DEBUG))
        file_handler.setFormatter(
            logging.Formatter(DEFAULT_FORMAT, DEFAULT_DATE_FORMAT)
        )
        self.logger.addHandler(file_handler)
    
    def debug(self, message: str) -> None:
        """Log debug message"""
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        """Log info message"""
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message"""
        self.logger.error(message)
    
    def critical(self, message: str) -> None:
        """Log critical message"""
        self.logger.critical(message)


# Module-level convenience function
def get_logger() -> ThalosLogger:
    """Get the singleton Thalos logger instance"""
    return ThalosLogger()
