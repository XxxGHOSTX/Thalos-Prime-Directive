# Thalos Prime v1.0 - conftest.py
# Pytest configuration and fixtures

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

import sys
import os
import pytest

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


@pytest.fixture
def cis():
    """Fixture providing a booted CIS instance"""
    from core.cis import CIS
    cis = CIS()
    cis.boot()
    yield cis
    cis.shutdown()


@pytest.fixture
def memory():
    """Fixture providing a Memory Module instance"""
    from core.memory import MemoryModule
    return MemoryModule()


@pytest.fixture
def codegen():
    """Fixture providing a Code Generator instance"""
    from codegen import CodeGenerator
    return CodeGenerator()


@pytest.fixture
def cli(cis):
    """Fixture providing a CLI instance with booted CIS"""
    from interfaces.cli import CLI
    return CLI(cis)


@pytest.fixture
def api(cis):
    """Fixture providing an API instance with booted CIS"""
    from interfaces.api import API
    return API(cis)


@pytest.fixture
def clean_memory():
    """Fixture providing a fresh Memory Module for each test"""
    from core.memory import MemoryModule
    mem = MemoryModule()
    yield mem
    mem.clear()


@pytest.fixture
def codegen_with_history():
    """Fixture providing a Code Generator with history tracking enabled"""
    from codegen import CodeGenerator
    gen = CodeGenerator(track_history=True)
    yield gen
    gen.clear_history()
