#!/bin/bash
# © 2026 Tony Ray Macier III. All rights reserved.
# Thalos Prime™ is a proprietary system.

# Thalos Prime Web Deployment Startup Script
# Production-ready launcher with automatic dependency management

set -e

# Banner
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║                                                                  ║"
echo "║  ████████╗██╗  ██╗ █████╗ ██╗      ██████╗ ███████╗            ║"
echo "║  ╚══██╔══╝██║  ██║██╔══██╗██║     ██╔═══██╗██╔════╝            ║"
echo "║     ██║   ███████║███████║██║     ██║   ██║███████╗            ║"
echo "║     ██║   ██╔══██║██╔══██║██║     ██║   ██║╚════██║            ║"
echo "║     ██║   ██║  ██║██║  ██║███████╗╚██████╔╝███████║            ║"
echo "║     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝            ║"
echo "║                                                                  ║"
echo "║              PRIME v3.0 - WEB DEPLOYMENT EDITION                ║"
echo "║          Synthetic Biological Intelligence System               ║"
echo "║                                                                  ║"
echo "║        © 2026 Tony Ray Macier III. All rights reserved.        ║"
echo "║                                                                  ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.12+"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check/install dependencies
echo "📦 Checking dependencies..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing Flask..."
    pip install -q flask flask-cors
fi

if ! python3 -c "import numpy" 2>/dev/null; then
    echo "Installing NumPy..."
    pip install -q numpy scipy
fi

echo "✓ All dependencies ready"
echo ""

# Create necessary directories
mkdir -p data logs data/storage
echo "✓ Data directories ready"
echo ""

# Setup environment
if [ ! -f .env ]; then
    echo "📝 Creating .env configuration..."
    cp .env.example .env
    echo "✓ Environment configured"
else
    echo "✓ Environment already configured"
fi
echo ""

# Start the web interface
echo "🚀 Starting Thalos Prime Web Interface..."
echo "=================================================================="
echo ""

# Use boot_thalos.py for the immersive experience
python3 boot_thalos.py
