# Thalos Prime v1.0 - API Reference

---

**© 2026 Tony Ray Macier III. All rights reserved.**

This document is part of Thalos Prime, an original proprietary software system. Unauthorized reproduction, modification, distribution, or use is strictly prohibited without express written permission.

**Thalos Prime™ is a proprietary system.**

---

## Overview

This document provides a complete API reference for Thalos Prime v1.0, covering both the programmatic Python API and the REST HTTP interface.

## Table of Contents

1. [Python API](#python-api)
   - [CIS (Central Intelligence System)](#cis-central-intelligence-system)
   - [Memory Module](#memory-module)
   - [Code Generator](#code-generator)
   - [CLI Interface](#cli-interface)
   - [API Interface](#api-interface)
2. [REST API](#rest-api)
   - [System Endpoints](#system-endpoints)
   - [Memory Endpoints](#memory-endpoints)
   - [CodeGen Endpoints](#codegen-endpoints)
3. [CLI Commands](#cli-commands)

---

## Python API

### CIS (Central Intelligence System)

The Central Intelligence System is the primary orchestrator for Thalos Prime.

#### Import

```python
from core.cis import CIS
```

#### Class: `CIS`

##### Constructor

```python
CIS()
```

Creates a new CIS instance. The system is created but not booted.

##### Methods

###### `boot() -> bool`

Boot the system, initializing all subsystems.

**Returns**: `True` if boot successful, `False` if already booted.

```python
cis = CIS()
result = cis.boot()  # True
```

###### `shutdown() -> bool`

Shutdown the system, clearing all subsystems.

**Returns**: `True` if shutdown successful, `False` if not booted.

```python
cis.shutdown()  # True
```

###### `status() -> Dict[str, Any]`

Get current system status.

**Returns**: Dictionary with version, status, booted flag, and subsystems.

```python
status = cis.status()
# {
#     'version': '1.0',
#     'status': 'operational',
#     'booted': True,
#     'subsystems': {
#         'memory': True,
#         'codegen': True,
#         'cli': True,
#         'api': True
#     }
# }
```

###### `get_memory() -> Optional[MemoryModule]`

Get the Memory subsystem instance.

**Returns**: `MemoryModule` if booted, `None` otherwise.

###### `get_codegen() -> Optional[CodeGenerator]`

Get the CodeGen subsystem instance.

**Returns**: `CodeGenerator` if booted, `None` otherwise.

###### `get_cli() -> Optional[CLI]`

Get the CLI interface instance.

**Returns**: `CLI` if booted, `None` otherwise.

###### `get_api() -> Optional[API]`

Get the API interface instance.

**Returns**: `API` if booted, `None` otherwise.

---

### Memory Module

In-memory key-value storage with explicit CRUD operations.

#### Import

```python
from core.memory import MemoryModule
```

#### Class: `MemoryModule`

##### Methods

###### `create(key: str, value: Any) -> bool`

Create a new entry in storage.

**Parameters**:
- `key`: Unique identifier for the data
- `value`: Data to store

**Returns**: `True` if created, `False` if key already exists.

```python
memory.create('user:1', {'name': 'John'})  # True
memory.create('user:1', {'name': 'Jane'})  # False (exists)
```

###### `read(key: str) -> Optional[Any]`

Read data from storage.

**Parameters**:
- `key`: Key to read

**Returns**: Stored value or `None` if not found.

```python
value = memory.read('user:1')  # {'name': 'John'}
value = memory.read('missing')  # None
```

###### `update(key: str, value: Any) -> bool`

Update existing data in storage.

**Parameters**:
- `key`: Key to update
- `value`: New value

**Returns**: `True` if updated, `False` if key doesn't exist.

```python
memory.update('user:1', {'name': 'Jane'})  # True
memory.update('missing', {'name': 'X'})  # False
```

###### `delete(key: str) -> bool`

Delete data from storage.

**Parameters**:
- `key`: Key to delete

**Returns**: `True` if deleted, `False` if key doesn't exist.

```python
memory.delete('user:1')  # True
memory.delete('missing')  # False
```

###### `exists(key: str) -> bool`

Check if a key exists.

**Parameters**:
- `key`: Key to check

**Returns**: `True` if exists, `False` otherwise.

```python
memory.exists('user:1')  # True
```

###### `list_keys() -> List[str]`

List all stored keys.

**Returns**: List of all keys in storage.

```python
keys = memory.list_keys()  # ['user:1', 'user:2', ...]
```

###### `count() -> int`

Get count of stored items.

**Returns**: Number of items in storage.

```python
count = memory.count()  # 5
```

###### `clear() -> None`

Clear all data from storage.

```python
memory.clear()
```

---

### Code Generator

Deterministic code generation engine.

#### Import

```python
from codegen import CodeGenerator
```

#### Class: `CodeGenerator`

##### Constructor

```python
CodeGenerator(track_history: bool = False)
```

**Parameters**:
- `track_history`: Enable generation history tracking

##### Methods

###### `register_template(name: str, content: str) -> bool`

Register a code template.

**Parameters**:
- `name`: Template name
- `content`: Template string with `{placeholders}`

**Returns**: `True` if registered, `False` if already exists.

```python
codegen.register_template('class', 'class {name}:\n    pass')  # True
```

###### `generate(template_name: str, context: Dict[str, Any]) -> Optional[str]`

Generate code from a template.

**Parameters**:
- `template_name`: Name of registered template
- `context`: Dictionary of placeholder values

**Returns**: Generated code string or `None` if template not found.

```python
code = codegen.generate('class', {'name': 'User'})
# 'class User:\n    pass'
```

###### `generate_class(name: str, methods: List[str] = None) -> str`

Generate a Python class structure.

**Parameters**:
- `name`: Class name
- `methods`: List of method names (default: `['__init__']`)

**Returns**: Generated class code.

```python
code = codegen.generate_class('User', ['save', 'load'])
# class User:
#     """Auto-generated User class"""
#
#     def __init__(self):
#         """Initialize User"""
#         pass
#
#     def save(self):
#         """Auto-generated save method"""
#         pass
#
#     def load(self):
#         """Auto-generated load method"""
#         pass
```

###### `generate_function(name: str, parameters: List[str] = None) -> str`

Generate a Python function structure.

**Parameters**:
- `name`: Function name
- `parameters`: List of parameter names

**Returns**: Generated function code.

```python
code = codegen.generate_function('process', ['data', 'config'])
# def process(data, config):
#     """Auto-generated process function"""
#     pass
```

###### `list_templates() -> List[str]`

List registered templates (sorted).

**Returns**: Sorted list of template names.

###### `get_history() -> List[Dict]`

Get generation history (if tracking enabled).

**Returns**: List of generation records.

###### `clear_history() -> None`

Clear generation history.

---

### CLI Interface

Command-line interface for Thalos Prime.

#### Import

```python
from interfaces.cli import CLI
```

#### Class: `CLI`

##### Constructor

```python
CLI(cis: Optional[CIS] = None)
```

**Parameters**:
- `cis`: CIS instance to delegate to

##### Methods

###### `execute(args: List[str]) -> str`

Execute a CLI command.

**Parameters**:
- `args`: Command-line arguments

**Returns**: Result message string.

```python
cli = CLI(cis)
result = cli.execute(['status'])
result = cli.execute(['memory', 'create', 'key', 'value'])
```

###### `set_cis(cis: CIS) -> None`

Set the CIS instance.

---

### API Interface

REST API interface for Thalos Prime.

#### Import

```python
from interfaces.api import API
```

#### Class: `API`

##### Constructor

```python
API(cis: Optional[CIS] = None)
```

##### Methods

###### `handle_request(method: str, path: str, body: Optional[Dict] = None) -> Dict`

Handle an API request.

**Parameters**:
- `method`: HTTP method (GET, POST, PUT, DELETE)
- `path`: Request path
- `body`: Optional request body

**Returns**: Response dictionary with status, code, and data.

```python
api = API(cis)
response = api.handle_request('GET', '/status')
response = api.handle_request('POST', '/memory', {'key': 'k1', 'value': 'v1'})
```

---

## REST API

### Response Format

All API responses follow this format:

```json
{
    "status": "success" | "error",
    "code": 200,
    "data": { ... } | null,
    "message": "Error message" (only on error)
}
```

### System Endpoints

#### GET /health

Health check endpoint.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "healthy": true,
        "service": "Thalos Prime",
        "version": "1.0"
    }
}
```

#### GET /status

Get system status.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "version": "1.0",
        "status": "operational",
        "booted": true,
        "subsystems": {
            "memory": true,
            "codegen": true,
            "cli": true,
            "api": true
        }
    }
}
```

#### POST /boot

Boot the system.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "booted": true
    }
}
```

#### POST /shutdown

Shutdown the system.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "shutdown": true
    }
}
```

### Memory Endpoints

#### POST /memory

Create a new memory entry.

**Request Body**:
```json
{
    "key": "mykey",
    "value": "myvalue"
}
```

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "created": true
    }
}
```

#### GET /memory/{key}

Read a memory entry.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "key": "mykey",
        "value": "myvalue"
    }
}
```

#### PUT /memory/{key}

Update a memory entry.

**Request Body**:
```json
{
    "value": "newvalue"
}
```

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "updated": true
    }
}
```

#### DELETE /memory/{key}

Delete a memory entry.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "deleted": true
    }
}
```

#### GET /memory

List all memory keys.

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "keys": ["key1", "key2"],
        "count": 2
    }
}
```

### CodeGen Endpoints

#### POST /codegen/class

Generate a Python class.

**Request Body**:
```json
{
    "name": "MyClass",
    "methods": ["process", "validate"]
}
```

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "code": "class MyClass:\n    ..."
    }
}
```

#### POST /codegen/function

Generate a Python function.

**Request Body**:
```json
{
    "name": "process_data",
    "parameters": ["input", "config"]
}
```

**Response**:
```json
{
    "status": "success",
    "code": 200,
    "data": {
        "code": "def process_data(input, config):\n    ..."
    }
}
```

---

## CLI Commands

### System Commands

```bash
# Boot the system
python src/main.py boot

# Shutdown the system
python src/main.py shutdown

# Get system status
python src/main.py status
```

### Memory Commands

```bash
# Create entry
python src/main.py memory create <key> <value>

# Read entry
python src/main.py memory read <key>

# Update entry
python src/main.py memory update <key> <value>

# Delete entry
python src/main.py memory delete <key>

# List all keys
python src/main.py memory list

# Get count
python src/main.py memory count
```

### CodeGen Commands

```bash
# Generate class
python src/main.py codegen class <ClassName> [--methods method1 method2]

# Generate function
python src/main.py codegen function <function_name> [--params param1 param2]
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request (missing parameters) |
| 404 | Not Found (key/endpoint not found) |
| 405 | Method Not Allowed |
| 409 | Conflict (key already exists) |
| 500 | Internal Server Error (CIS not initialized) |

---

**Version**: 1.0  
**Last Updated**: 2026-01-16  
**Status**: Complete
