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
Thalos Prime v1.0 - Configuration Module

Provides configuration management for the Thalos Prime system.
Reads from config/thalos.conf with deterministic default values.
"""

import os
import configparser
from typing import Dict, Any, Optional


class ThalosConfig:
    """
    Configuration manager for Thalos Prime
    
    Provides:
    - INI file parsing
    - Default value handling
    - Type conversion
    - Section-based organization
    """
    
    # Default configuration values
    DEFAULTS: Dict[str, Dict[str, Any]] = {
        'system': {
            'version': '1.0',
            'name': 'ThalosPrime'
        },
        'cis': {
            'enabled': True
        },
        'memory': {
            'enabled': True
        },
        'interfaces': {
            'cli_enabled': True,
            'api_enabled': True
        },
        'codegen': {
            'deterministic': True
        }
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration
        
        Args:
            config_path: Path to config file (optional)
        """
        self.config = configparser.ConfigParser()
        self.config_path = config_path
        
        # Apply defaults
        for section, values in self.DEFAULTS.items():
            if not self.config.has_section(section):
                self.config.add_section(section)
            for key, value in values.items():
                self.config.set(section, key, str(value))
        
        # Load config file if provided
        if config_path and os.path.exists(config_path):
            self.load(config_path)
    
    def load(self, config_path: str) -> bool:
        """
        Load configuration from file
        
        Args:
            config_path: Path to configuration file
            
        Returns:
            bool: True if loaded successfully
        """
        if not os.path.exists(config_path):
            return False
        
        try:
            self.config.read(config_path)
            self.config_path = config_path
            return True
        except configparser.Error:
            return False
    
    def get(self, section: str, key: str, fallback: Any = None) -> str:
        """
        Get a configuration value
        
        Args:
            section: Configuration section
            key: Configuration key
            fallback: Default value if not found
            
        Returns:
            Configuration value as string
        """
        return self.config.get(section, key, fallback=fallback)
    
    def get_bool(self, section: str, key: str, fallback: bool = False) -> bool:
        """
        Get a boolean configuration value
        
        Args:
            section: Configuration section
            key: Configuration key
            fallback: Default value if not found
            
        Returns:
            Configuration value as boolean
        """
        return self.config.getboolean(section, key, fallback=fallback)
    
    def get_int(self, section: str, key: str, fallback: int = 0) -> int:
        """
        Get an integer configuration value
        
        Args:
            section: Configuration section
            key: Configuration key
            fallback: Default value if not found
            
        Returns:
            Configuration value as integer
        """
        return self.config.getint(section, key, fallback=fallback)
    
    def get_section(self, section: str) -> Dict[str, str]:
        """
        Get all values in a section
        
        Args:
            section: Configuration section
            
        Returns:
            Dictionary of key-value pairs
        """
        if not self.config.has_section(section):
            return {}
        return dict(self.config.items(section))
    
    def set(self, section: str, key: str, value: Any) -> None:
        """
        Set a configuration value
        
        Args:
            section: Configuration section
            key: Configuration key
            value: Value to set
        """
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))
    
    def save(self, config_path: Optional[str] = None) -> bool:
        """
        Save configuration to file
        
        Args:
            config_path: Path to save to (uses loaded path if not specified)
            
        Returns:
            bool: True if saved successfully
        """
        path = config_path or self.config_path
        if not path:
            return False
        
        try:
            with open(path, 'w') as f:
                self.config.write(f)
            return True
        except IOError:
            return False
    
    def to_dict(self) -> Dict[str, Dict[str, str]]:
        """
        Export configuration as dictionary
        
        Returns:
            Nested dictionary of all configuration values
        """
        result = {}
        for section in self.config.sections():
            result[section] = dict(self.config.items(section))
        return result


# Module-level convenience function
def load_config(config_path: Optional[str] = None) -> ThalosConfig:
    """
    Load configuration from default or specified path
    
    Args:
        config_path: Optional path to config file
        
    Returns:
        ThalosConfig instance
    """
    if config_path is None:
        # Try to find default config path
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        config_path = os.path.join(base_dir, 'config', 'thalos.conf')
    
    return ThalosConfig(config_path)
