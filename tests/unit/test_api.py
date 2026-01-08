"""
Thalos Prime v1.0 - Unit Tests for API

Tests for stateless REST API with minimal surface
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from core.cis import CIS
from interfaces.api import API


def test_api_initialization():
    """Test API initialization"""
    api = API()
    assert api is not None
    assert api.cis is None
    print("✓ API initialization test passed")


def test_api_with_cis():
    """Test API initialization with CIS"""
    cis = CIS()
    api = API(cis)
    assert api.cis is not None
    print("✓ API with CIS test passed")


def test_set_cis():
    """Test setting CIS after initialization"""
    api = API()
    cis = CIS()
    api.set_cis(cis)
    assert api.cis == cis
    print("✓ Set CIS test passed")


def test_health_endpoint():
    """Test health check endpoint"""
    api = API()
    
    response = api.handle_request('GET', '/health')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['healthy'] is True
    assert response['data']['service'] == 'Thalos Prime'
    
    print("✓ Health endpoint test passed")


def test_status_endpoint():
    """Test status endpoint delegates to CIS"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    response = api.handle_request('GET', '/status')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert 'version' in response['data']
    assert response['data']['version'] == '1.0'
    
    print("✓ Status endpoint test passed")


def test_boot_endpoint():
    """Test boot endpoint delegates to CIS"""
    cis = CIS()
    api = API(cis)
    
    response = api.handle_request('POST', '/boot')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['booted'] is True
    
    print("✓ Boot endpoint test passed")


def test_shutdown_endpoint():
    """Test shutdown endpoint delegates to CIS"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    response = api.handle_request('POST', '/shutdown')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['shutdown'] is True
    
    print("✓ Shutdown endpoint test passed")


def test_memory_create_endpoint():
    """Test memory create endpoint (POST /memory)"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    response = api.handle_request('POST', '/memory', {'key': 'testkey', 'value': 'testvalue'})
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['created'] is True
    
    # Duplicate create should fail
    response = api.handle_request('POST', '/memory', {'key': 'testkey', 'value': 'other'})
    assert response['status'] == 'error'
    assert response['code'] == 409
    
    print("✓ Memory create endpoint test passed")


def test_memory_read_endpoint():
    """Test memory read endpoint (GET /memory/{key})"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # Create data first
    api.handle_request('POST', '/memory', {'key': 'testkey', 'value': 'testvalue'})
    
    # Read it
    response = api.handle_request('GET', '/memory/testkey')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['key'] == 'testkey'
    assert response['data']['value'] == 'testvalue'
    
    # Read non-existent
    response = api.handle_request('GET', '/memory/nonexistent')
    assert response['status'] == 'error'
    assert response['code'] == 404
    
    print("✓ Memory read endpoint test passed")


def test_memory_update_endpoint():
    """Test memory update endpoint (PUT /memory/{key})"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # Create data first
    api.handle_request('POST', '/memory', {'key': 'testkey', 'value': 'initial'})
    
    # Update it
    response = api.handle_request('PUT', '/memory/testkey', {'value': 'updated'})
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['updated'] is True
    
    # Verify update
    response = api.handle_request('GET', '/memory/testkey')
    assert response['data']['value'] == 'updated'
    
    print("✓ Memory update endpoint test passed")


def test_memory_delete_endpoint():
    """Test memory delete endpoint (DELETE /memory/{key})"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # Create data first
    api.handle_request('POST', '/memory', {'key': 'testkey', 'value': 'testvalue'})
    
    # Delete it
    response = api.handle_request('DELETE', '/memory/testkey')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert response['data']['deleted'] is True
    
    # Verify deletion
    response = api.handle_request('GET', '/memory/testkey')
    assert response['code'] == 404
    
    print("✓ Memory delete endpoint test passed")


def test_memory_list_endpoint():
    """Test memory list endpoint (GET /memory)"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # Create some data
    api.handle_request('POST', '/memory', {'key': 'k1', 'value': 'v1'})
    api.handle_request('POST', '/memory', {'key': 'k2', 'value': 'v2'})
    
    # List keys
    response = api.handle_request('GET', '/memory')
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert 'k1' in response['data']['keys']
    assert 'k2' in response['data']['keys']
    assert response['data']['count'] == 2
    
    print("✓ Memory list endpoint test passed")


def test_codegen_class_endpoint():
    """Test codegen class endpoint (POST /codegen/class)"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    response = api.handle_request('POST', '/codegen/class', {'name': 'TestClass'})
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert 'class TestClass:' in response['data']['code']
    
    # With methods
    response = api.handle_request('POST', '/codegen/class', {'name': 'TestClass', 'methods': ['process', 'validate']})
    assert 'def process' in response['data']['code']
    assert 'def validate' in response['data']['code']
    
    print("✓ Codegen class endpoint test passed")


def test_codegen_function_endpoint():
    """Test codegen function endpoint (POST /codegen/function)"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    response = api.handle_request('POST', '/codegen/function', {'name': 'test_func'})
    assert response['status'] == 'success'
    assert response['code'] == 200
    assert 'def test_func' in response['data']['code']
    
    # With parameters
    response = api.handle_request('POST', '/codegen/function', {'name': 'process', 'parameters': ['data', 'config']})
    assert 'def process(data, config):' in response['data']['code']
    
    print("✓ Codegen function endpoint test passed")


def test_unknown_endpoint():
    """Test unknown endpoint returns 404"""
    api = API()
    
    response = api.handle_request('GET', '/unknown')
    assert response['status'] == 'error'
    assert response['code'] == 404
    
    print("✓ Unknown endpoint test passed")


def test_stateless_api():
    """Test that API is stateless"""
    cis = CIS()
    cis.boot()
    
    # Create two API instances with same CIS
    api1 = API(cis)
    api2 = API(cis)
    
    # Create data through api1
    api1.handle_request('POST', '/memory', {'key': 'k1', 'value': 'v1'})
    
    # Read through api2 (should work because data is in CIS, not API)
    response = api2.handle_request('GET', '/memory/k1')
    assert response['status'] == 'success'
    assert response['data']['value'] == 'v1'
    
    print("✓ Stateless API test passed")


def test_api_delegation():
    """Test that API delegates all operations to CIS"""
    cis = CIS()
    cis.boot()
    api = API(cis)
    
    # All operations should go through CIS subsystems
    # Memory operations
    api.handle_request('POST', '/memory', {'key': 'k1', 'value': 'v1'})
    
    # Verify directly in CIS memory
    memory = cis.get_memory()
    assert memory.read('k1') == 'v1'
    
    print("✓ API delegation test passed")


if __name__ == '__main__':
    print("Running API Unit Tests...")
    test_api_initialization()
    test_api_with_cis()
    test_set_cis()
    test_health_endpoint()
    test_status_endpoint()
    test_boot_endpoint()
    test_shutdown_endpoint()
    test_memory_create_endpoint()
    test_memory_read_endpoint()
    test_memory_update_endpoint()
    test_memory_delete_endpoint()
    test_memory_list_endpoint()
    test_codegen_class_endpoint()
    test_codegen_function_endpoint()
    test_unknown_endpoint()
    test_stateless_api()
    test_api_delegation()
    print("\nAll API tests passed!")
