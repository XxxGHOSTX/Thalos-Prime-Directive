"""
Thalos Prime v1.0 - Integration Tests

Tests for system integrity with all components working together
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.cis import CIS
from interfaces.cli import CLI
from interfaces.api import API


def test_full_system_lifecycle():
    """Test complete system lifecycle from creation to shutdown"""
    print("Testing full system lifecycle...")
    
    # Create CIS
    cis = CIS()
    assert cis.status()['status'] == 'created'
    
    # Boot system
    assert cis.boot() is True
    assert cis.status()['status'] == 'operational'
    assert cis.status()['booted'] is True
    
    # Verify all subsystems initialized
    assert cis.get_memory() is not None
    assert cis.get_codegen() is not None
    assert cis.get_cli() is not None
    assert cis.get_api() is not None
    
    # Shutdown system
    assert cis.shutdown() is True
    assert cis.status()['status'] == 'shutdown'
    assert cis.status()['booted'] is False
    
    print("✓ Full system lifecycle test passed")


def test_memory_through_cis():
    """Test memory operations through CIS"""
    print("Testing memory through CIS...")
    
    cis = CIS()
    cis.boot()
    memory = cis.get_memory()
    
    # CRUD operations
    assert memory.create('key1', 'value1') is True
    assert memory.read('key1') == 'value1'
    assert memory.update('key1', 'value2') is True
    assert memory.read('key1') == 'value2'
    assert memory.delete('key1') is True
    assert memory.exists('key1') is False
    
    print("✓ Memory through CIS test passed")


def test_codegen_through_cis():
    """Test code generation through CIS"""
    print("Testing codegen through CIS...")
    
    cis = CIS()
    cis.boot()
    codegen = cis.get_codegen()
    
    # Generate class
    code = codegen.generate_class('TestClass', ['method1', 'method2'])
    assert 'class TestClass:' in code
    assert 'def method1' in code
    assert 'def method2' in code
    
    # Generate function
    code = codegen.generate_function('test_func', ['arg1', 'arg2'])
    assert 'def test_func(arg1, arg2):' in code
    
    print("✓ Codegen through CIS test passed")


def test_cli_integration():
    """Test CLI integration with full system"""
    print("Testing CLI integration...")
    
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    
    # Status command
    result = cli.execute(['status'])
    assert 'operational' in result
    
    # Memory commands
    cli.execute(['memory', 'create', 'k1', 'v1'])
    result = cli.execute(['memory', 'read', 'k1'])
    assert 'v1' in result
    
    # Codegen command
    result = cli.execute(['codegen', 'class', 'MyClass'])
    assert 'class MyClass:' in result
    
    print("✓ CLI integration test passed")


def test_api_integration():
    """Test API integration with full system"""
    print("Testing API integration...")
    
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # Health check
    response = api.handle_request('GET', '/health')
    assert response['status'] == 'success'
    
    # Status
    response = api.handle_request('GET', '/status')
    assert response['data']['status'] == 'operational'
    
    # Memory operations
    response = api.handle_request('POST', '/memory', {'key': 'k1', 'value': 'v1'})
    assert response['status'] == 'success'
    
    response = api.handle_request('GET', '/memory/k1')
    assert response['data']['value'] == 'v1'
    
    # Codegen operations
    response = api.handle_request('POST', '/codegen/class', {'name': 'TestClass'})
    assert 'class TestClass:' in response['data']['code']
    
    print("✓ API integration test passed")


def test_cli_and_api_interoperability():
    """Test that CLI and API can operate on same data through CIS"""
    print("Testing CLI and API interoperability...")
    
    cis = CIS()
    cis.boot()
    cli = CLI(cis)
    api = API(cis)
    
    # Create data via CLI
    cli.execute(['memory', 'create', 'shared_key', 'cli_value'])
    
    # Read via API
    response = api.handle_request('GET', '/memory/shared_key')
    assert response['data']['value'] == 'cli_value'
    
    # Update via API
    api.handle_request('PUT', '/memory/shared_key', {'value': 'api_value'})
    
    # Read via CLI
    result = cli.execute(['memory', 'read', 'shared_key'])
    assert 'api_value' in result
    
    print("✓ CLI and API interoperability test passed")


def test_deterministic_behavior_across_instances():
    """Test deterministic behavior across different system instances"""
    print("Testing deterministic behavior...")
    
    # System 1
    cis1 = CIS()
    cis1.boot()
    mem1 = cis1.get_memory()
    codegen1 = cis1.get_codegen()
    
    # System 2
    cis2 = CIS()
    cis2.boot()
    mem2 = cis2.get_memory()
    codegen2 = cis2.get_codegen()
    
    # Same operations should produce same results
    mem1.create('k1', 'v1')
    mem2.create('k1', 'v1')
    assert mem1.read('k1') == mem2.read('k1')
    
    code1 = codegen1.generate_class('Test', ['m1', 'm2'])
    code2 = codegen2.generate_class('Test', ['m1', 'm2'])
    assert code1 == code2
    
    print("✓ Deterministic behavior test passed")


def test_authority_hierarchy():
    """Test that CIS maintains authority over all subsystems"""
    print("Testing authority hierarchy...")
    
    cis = CIS()
    cis.boot()
    
    # All subsystems should be accessible through CIS
    memory = cis.get_memory()
    codegen = cis.get_codegen()
    cli = cis.get_cli()
    api = cis.get_api()
    
    assert memory is not None
    assert codegen is not None
    assert cli is not None
    assert api is not None
    
    # After shutdown, subsystems should be cleared
    cis.shutdown()
    assert cis.get_memory() is None
    assert cis.get_codegen() is None
    
    print("✓ Authority hierarchy test passed")


def test_explicit_state_management():
    """Test that all state changes are explicit and traceable"""
    print("Testing explicit state management...")
    
    cis = CIS()
    
    # Initial state
    status = cis.status()
    assert status['booted'] is False
    
    # Boot - explicit state change
    cis.boot()
    status = cis.status()
    assert status['booted'] is True
    assert status['status'] == 'operational'
    
    # Memory operations - explicit CRUD
    memory = cis.get_memory()
    assert memory.create('k1', 'v1') is True  # Explicit success
    assert memory.create('k1', 'v2') is False  # Explicit failure
    
    # Shutdown - explicit state change
    cis.shutdown()
    status = cis.status()
    assert status['booted'] is False
    assert status['status'] == 'shutdown'
    
    print("✓ Explicit state management test passed")


def test_no_hidden_state():
    """Test that there is no hidden state in the system"""
    print("Testing no hidden state...")
    
    cis = CIS()
    cis.boot()
    
    # All state should be accessible through status
    status = cis.status()
    assert 'version' in status
    assert 'status' in status
    assert 'booted' in status
    assert 'subsystems' in status
    
    # Memory state should be accessible
    memory = cis.get_memory()
    memory.create('k1', 'v1')
    assert memory.count() == 1
    assert 'k1' in memory.list_keys()
    
    print("✓ No hidden state test passed")


def test_isolation_and_modularity():
    """Test that components are properly isolated and modular"""
    print("Testing isolation and modularity...")
    
    # Codegen should work without CIS
    from codegen import CodeGenerator
    codegen = CodeGenerator()
    code = codegen.generate_class('Standalone')
    assert 'class Standalone:' in code
    
    # Memory should work without CIS
    from core.memory import MemoryModule
    memory = MemoryModule()
    memory.create('k1', 'v1')
    assert memory.read('k1') == 'v1'
    
    print("✓ Isolation and modularity test passed")


def test_error_handling_and_recovery():
    """Test proper error handling and system recovery"""
    print("Testing error handling...")
    
    cis = CIS()
    
    # Cannot shutdown before boot
    assert cis.shutdown() is False
    
    # Cannot boot twice
    cis.boot()
    assert cis.boot() is False
    
    # Operations before boot should fail gracefully
    cis2 = CIS()
    cli = CLI(cis2)
    result = cli.execute(['memory', 'list'])
    assert 'not initialized' in result.lower() or 'boot' in result.lower()
    
    print("✓ Error handling test passed")


if __name__ == '__main__':
    print("=== Running Thalos Prime Integration Tests ===\n")
    
    test_full_system_lifecycle()
    test_memory_through_cis()
    test_codegen_through_cis()
    test_cli_integration()
    test_api_integration()
    test_cli_and_api_interoperability()
    test_deterministic_behavior_across_instances()
    test_authority_hierarchy()
    test_explicit_state_management()
    test_no_hidden_state()
    test_isolation_and_modularity()
    test_error_handling_and_recovery()
    
    print("\n=== All Integration Tests Passed! ===")
