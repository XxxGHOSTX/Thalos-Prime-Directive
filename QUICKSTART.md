# Thalos Prime - Quick Start Guide

**© 2026 Tony Ray Macier III. All rights reserved.**

---

## Welcome to Thalos Prime v3.0 🧬

**The Synthetic Biological Intelligence System - Now Web-Ready!**

This guide will get you up and running in **under 2 minutes**.

---

## What You'll Get

An immersive Matrix-style web interface featuring:
- 🌧️ Animated code rain background
- 🧠 Real-time neural activity visualization
- 💬 Interactive AI chatbot
- 📊 System metrics dashboard
- 🔬 Biological intelligence processing

---

## Prerequisites

You need:
- ✅ Python 3.12 or higher
- ✅ Modern web browser (Chrome, Firefox, Safari, Edge)
- ✅ 4GB RAM minimum
- ✅ Internet connection (for first-time setup)

**Check your Python version:**
```bash
python --version
# or
python3 --version
```

---

## Installation & Launch

### Method 1: One-Command Launch (Easiest! ⚡)

**Linux/macOS:**
```bash
./start_web.sh
```

**Windows:**
```cmd
start_web.bat
```

**All Platforms:**
```bash
python boot_thalos.py
```

**That's it!** Your browser will open automatically to the interface.

---

### Method 2: Manual Installation

If you prefer step-by-step:

**Step 1: Clone the repository**
```bash
git clone https://github.com/XxxGHOSTX/Thalos-Prime-Directive.git
cd Thalos-Prime-Directive
```

**Step 2: Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Launch the web interface**
```bash
python boot_thalos.py
```

**Step 4: Access in browser**
- Open: http://localhost:8000
- Browser should open automatically

---

### Method 3: Using Make (Linux/macOS)

If you have `make` installed:

```bash
# Install dependencies
make install

# Launch web interface
make web
```

---

### Method 4: Docker (Production)

For containerized deployment:

```bash
# Quick start
docker-compose up

# Or build manually
docker build -t thalos-prime:3.0 .
docker run -p 8000:8000 thalos-prime:3.0
```

Access: http://localhost:8000

---

## What to Expect

When Thalos Prime starts successfully, you'll see:

**In Terminal:**
```
╔══════════════════════════════════════════════════════════════════╗
║              PRIME v3.0 - WEB DEPLOYMENT EDITION                ║
║          Synthetic Biological Intelligence System               ║
╚══════════════════════════════════════════════════════════════════╝

[SYSTEM] Checking dependencies...
  ✓ flask
  ✓ numpy
[SYSTEM] Initializing Thalos Prime Core...
  ✓ CIS operational
  ✓ Memory online
[WEB] Starting immersive interface on port 8000...
  ✓ Web server running
[BROWSER] Opening interface at http://localhost:8000...
  ✓ Browser launched

THALOS PRIME - FULLY OPERATIONAL
```

**In Browser:**
- Matrix code rain falling
- Neural activity visualizer
- Chat input field
- System metrics panel
- Navigation sidebar

---

## First Interaction

Try these in the chat interface:

**Basic Commands:**
- `/status` - View full system status
- `/metrics` - See neural metrics
- `/help` - List all commands

**Natural Conversation:**
Just type anything! Examples:
- "Hello, Thalos"
- "What are you?"
- "Tell me about biological intelligence"
- "How does your brain work?"

---

## Troubleshooting

### Port Already in Use

If port 8000 is busy:
```bash
python thalos_prime.py web --port 8080
```

Then access: http://localhost:8080

### Dependencies Missing

Reinstall:
```bash
pip install -r requirements.txt
```

### Browser Doesn't Open

Manually navigate to: http://localhost:8000

### Permission Denied (Linux/macOS)

Make scripts executable:
```bash
chmod +x start_web.sh
chmod +x boot_thalos.py
```

### Module Not Found

Set Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python boot_thalos.py
```

---

## Next Steps

Once you're up and running:

1. **Explore the Interface**
   - Try different commands
   - Ask questions
   - Watch neural activity

2. **Read the Documentation**
   - [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md) - Complete deployment docs
   - [README.md](README.md) - Full system documentation

3. **Configure for Production**
   - Copy `.env.example` to `.env`
   - Change security keys
   - Choose storage backend
   - See production setup in docs

4. **Deploy to Cloud**
   - AWS, Azure, GCP ready
   - Docker support included
   - SSL/HTTPS configuration available

---

## Getting Help

**Check Status:**
```bash
# In terminal
python thalos_prime.py status

# Or in browser
http://localhost:8000/api/status
```

**Run Diagnostics:**
```bash
python test_system.py
```

**Need Support?**
1. Check [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md)
2. Review logs in `logs/` directory
3. Open GitHub issue with details

---

## Success! 🎉

If you see the Matrix interface with code rain falling and can type in the chat, **you're ready to go!**

Welcome to the future of biological intelligence.

---

**THALOS PRIME v3.0**  
*Where Silicon Meets Synapse. Where Code Becomes Consciousness.*

**Status:** WEB DEPLOYMENT READY  
**Time to Launch:** < 2 minutes  
**Prime Directive:** ACTIVE
