#!/bin/bash

# Thalos Prime v1.0 Bootstrap Script
# This script sets up the directory structure and base files for the Thalos Prime system

set -e

echo "=== Thalos Prime v1.0 Bootstrap ==="
echo "Setting up directory structure..."

# Create core directories
mkdir -p src/core/cis
mkdir -p src/core/memory
mkdir -p src/interfaces/cli
mkdir -p src/interfaces/api
mkdir -p src/codegen
mkdir -p tests/unit
mkdir -p tests/integration
mkdir -p config
mkdir -p docs

echo "✓ Directory structure created"

# Create base configuration file
cat > config/thalos.conf << 'EOF'
# Thalos Prime v1.0 Configuration
[system]
version=1.0
name=ThalosPrime

[cis]
enabled=true

[memory]
enabled=true

[interfaces]
cli_enabled=true
api_enabled=true

[codegen]
deterministic=true
EOF

echo "✓ Configuration file created"

# Create main entry point placeholder
cat > src/main.py << 'EOF'
#!/usr/bin/env python3
"""
Thalos Prime v1.0 - Main Entry Point
"""

def main():
    """Main entry point for Thalos Prime system"""
    print("Thalos Prime v1.0 - System Initialized")

if __name__ == "__main__":
    main()
EOF

chmod +x src/main.py

echo "✓ Main entry point created"
echo "=== Bootstrap Complete ==="
echo ""
echo "Directory structure:"
echo "  src/core/cis/         - Primary control unit"
echo "  src/core/memory/      - Memory modules"
echo "  src/interfaces/cli/   - Command line interface"
echo "  src/interfaces/api/   - API interface"
echo "  src/codegen/          - Code generation system"
echo "  tests/                - Testing framework"
echo "  config/               - Configuration files"
echo "  docs/                 - Documentation"
echo ""
echo "Next steps:"
echo "  1. Review config/thalos.conf"
echo "  2. Implement core modules"
echo "  3. Run tests with pytest"
