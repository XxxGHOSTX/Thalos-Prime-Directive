"""
Thalos Prime v1.0 - Unit Tests for CLI

Tests for thin CLI interface with delegation to CIS
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.cis import CIS
from interfaces.cli import CLI


def test_cli_initialization():
    """Test CLI initialization"""
    cli = CLI()
    assert cli is not None
    assert cli.cis is None
    assert cli.parser is not None
    print("✓ CLI initialization test passed")


def test_cli_with_cis():
    """Test CLI initialization with CIS"""
    cis = CIS()
    cli = CLI(cis)
    assert cli.cis is not None
    print("✓ CLI with CIS test passed")


def test_set_cis():
    """Test setting CIS after initialization"""
    cli = CLI()
    cis = CIS()
    cli.set_cis(cis)
    assert cli.cis == cis
    print("✓ Set CIS test passed")


def test_boot_command():
    """Test boot command delegates to CIS"""
    cis = CIS()
    cli = CLI(cis)
    
    result = cli.execute(['boot'])
    assert 'booted successfully' in result.lower()
    
    # Second boot should report already booted
    result = cli.execute(['boot'])
    assert 'already booted' in result.lower()
    
    print("✓ Boot command test passed")


def test_status_command():
    """Test status command delegates to CIS"""
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    
    result = cli.execute(['status'])
    assert 'Thalos Prime' in result
    assert 'Version' in result
    assert 'Status' in result
    
    print("✓ Status command test passed")


def test_memory_commands():
    """Test memory commands delegate to CIS memory subsystem"""
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    
    # Create
    result = cli.execute(['memory', 'create', 'testkey', 'testvalue'])
    assert 'Created' in result or 'testkey' in result
    
    # Read
    result = cli.execute(['memory', 'read', 'testkey'])
    assert 'testkey' in result
    assert 'testvalue' in result
    
    # Update
    result = cli.execute(['memory', 'update', 'testkey', 'newvalue'])
    assert 'Updated' in result or 'testkey' in result
    
    # List
    result = cli.execute(['memory', 'list'])
    assert 'testkey' in result
    
    # Count
    result = cli.execute(['memory', 'count'])
    assert 'Total items' in result or '1' in result
    
    # Delete
    result = cli.execute(['memory', 'delete', 'testkey'])
    assert 'Deleted' in result or 'testkey' in result
    
    print("✓ Memory commands test passed")


def test_codegen_commands():
    """Test codegen commands delegate to CIS codegen subsystem"""
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    
    # Generate class
    result = cli.execute(['codegen', 'class', 'MyClass'])
    assert 'class MyClass:' in result
    
    # Generate class with methods
    result = cli.execute(['codegen', 'class', 'MyClass', '--methods', 'process', 'validate'])
    assert 'class MyClass:' in result
    assert 'def process' in result
    assert 'def validate' in result
    
    # Generate function
    result = cli.execute(['codegen', 'function', 'my_function'])
    assert 'def my_function' in result
    
    # Generate function with parameters
    result = cli.execute(['codegen', 'function', 'process', '--params', 'data', 'config'])
    assert 'def process(data, config):' in result
    
    print("✓ Codegen commands test passed")


def test_cli_without_cis():
    """Test CLI fails gracefully without CIS"""
    cli = CLI()
    
    result = cli.execute(['status'])
    assert 'CIS not initialized' in result
    
    print("✓ CLI without CIS test passed")


def test_cli_before_boot():
    """Test CLI operations fail before system boot"""
    cis = CIS()  # Created but not booted
    cli = CLI(cis)
    
    # Memory command should fail
    result = cli.execute(['memory', 'list'])
    assert 'not initialized' in result.lower() or 'boot' in result.lower()
    
    print("✓ CLI before boot test passed")


def test_thin_interface():
    """Test that CLI is a thin interface with no business logic"""
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    
    # CLI should delegate all operations to CIS
    # Test that CLI doesn't maintain state
    cli.execute(['memory', 'create', 'k1', 'v1'])
    
    # Create new CLI instance with same CIS
    cli2 = CLI(cis)
    result = cli2.execute(['memory', 'read', 'k1'])
    
    # Should be able to read because data is in CIS, not CLI
    assert 'v1' in result
    
    print("✓ Thin interface test passed")


def test_argparse_integration():
    """Test that CLI uses argparse correctly"""
    cli = CLI()
    
    # Parser should exist
    assert cli.parser is not None
    
    # Should handle --help
    result = cli.execute(['--help'])
    assert 'usage:' in result.lower() or 'thalos' in result.lower()
    
    print("✓ Argparse integration test passed")


if __name__ == '__main__':
    print("Running CLI Unit Tests...")
    test_cli_initialization()
    test_cli_with_cis()
    test_set_cis()
    test_boot_command()
    test_status_command()
    test_memory_commands()
    test_codegen_commands()
    test_cli_without_cis()
    test_cli_before_boot()
    test_thin_interface()
    test_argparse_integration()
    print("\nAll CLI tests passed!")
