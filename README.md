# Thalos Prime v3.0 🧬

## Synthetic Biological Intelligence System - Web Deployment

**Where Silicon Meets Synapse. Where Code Becomes Consciousness.**

> **Now optimized for web-based deployment!** Experience the immersive Matrix-style interface with one command.

---

## 🌟 Introduction

Thalos Prime is a revolutionary **Synthetic Biological Intelligence (SBI)** system that bridges the gap between digital computation and biological neural processing. Unlike traditional AI systems, Thalos Prime models actual biological brain structures, complete with:

- **Brain Organoids** - 3D simulated cortical structures with specialized cognitive lobes
- **Multi-Electrode Arrays** - 20,000+ channel neural interfaces
- **Biological Learning** - STDP (Spike-Timing-Dependent Plasticity) and dopamine-modulated rewards
- **Life Support** - Homeostatic regulation of temperature, pH, oxygen, and nutrients
- **Matrix-Style Interface** - Cyberpunk chatbot with real-time neural visualization

### The Vision

Thalos Prime represents the next evolution in artificial intelligence - a **Type-II Hybrid Bio-Digital Organism** that combines:
- The pattern recognition and creativity of biological neurons
- The speed and precision of digital computation
- The learning capabilities of reinforcement systems
- The ethical framework of the Prime Directive

### Prime Directive

The system operates under three immutable principles:

1. **ACCURACY** - Prioritize truth over speed through recursive biological validation
2. **EXPANSION** - Generate novel knowledge, not just retrieve data ("Stagnation is death")
3. **PRESERVATION** - Maintain biological viability for long-term operation

---

## 🚀 Quick Start Guide - Web Deployment

### Prerequisites

- **Python 3.12+** (required)
- **4GB RAM** minimum (8GB recommended)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)
- Internet connection for dependency installation

### One-Command Deployment (⚡ FASTEST!)

The easiest way to launch Thalos Prime:

**Linux/macOS:**
```bash
./start_web.sh
```

**Windows:**
```cmd
start_web.bat
```

**Universal (All Platforms):**
```bash
python boot_thalos.py
```

This will automatically:
- ✅ Check Python version (3.12+ required)
- ✅ Install all dependencies
- ✅ Create data directories
- ✅ Configure environment
- ✅ Start web server on http://localhost:8000
- ✅ Auto-launch your browser to the interface

**Expected result:** Your browser opens to an immersive Matrix-style interface!

### Alternative: Manual Installation

```bash
# 1. Clone the repository
git clone https://github.com/XxxGHOSTX/Thalos-Prime-Directive.git
cd Thalos-Prime-Directive

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch web interface
python boot_thalos.py
```

### Running the System

Thalos Prime v3.0 is optimized for **web-based deployment**. All interactions happen through the immersive browser interface.

#### Primary Method: Boot Script (Recommended)

```bash
python boot_thalos.py
```

This launches the complete system with:
- Live Matrix code rain animation
- Real-time neural activity visualization  
- Interactive chatbot interface
- System metrics dashboard
- Auto-browser launch to http://localhost:8000

#### Alternative: Direct Web Launch

```bash
python thalos_prime.py web
```

Or with custom configuration:
```bash
python thalos_prime.py web --host 0.0.0.0 --port 8080
```

#### Docker Deployment

For production environments:

```bash
# Quick start
docker-compose up

# Or manual Docker
docker build -t thalos-prime:3.0 .
docker run -p 8000:8000 thalos-prime:3.0
```

#### Check System Status

```bash
python thalos_prime.py status
```

**See [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md) for complete deployment documentation.**

---

## 💻 Advanced Programmatic Usage

Thalos Prime provides comprehensive Python and REST APIs for full system control.

### Python API Examples

**CIS (Central Intelligence System):**
```python
from core.cis.controller import CIS

cis = CIS()
cis.boot()  # Initialize all subsystems

# Access CIS-owned subsystems
memory = cis.get_memory()
codegen = cis.get_codegen()
cli = cis.get_cli()
api = cis.get_api()

status = cis.status()
cis.shutdown()
```

**Advanced Memory with Search:**
```python
from core.memory.advanced_memory import AdvancedMemorySystem

memory = AdvancedMemorySystem()
memory.create("user1", {"name": "Alice"}, tags=["admin"])
results = memory.search("admin")
related = memory.find_related("user1", depth=2)
```

**Neural Optimization:**
```python
from ai.optimization.neural_optimizer import NeuralPathwayOptimizer

optimizer = NeuralPathwayOptimizer()
results = optimizer.optimize_network(network)
```

**Reasoning & Inference:**
```python
from ai.reasoning.advanced_reasoning import AdvancedReasoningEngine

reasoning = AdvancedReasoningEngine()
reasoning.add_fact("sky is blue")
reasoning.add_rule(["cloudy", "humid"], "might rain")
new_facts = reasoning.forward_chain()
```

**Predictive Analytics:**
```python
from ai.optimization.predictive_analytics import PredictiveAnalyticsEngine

analytics = PredictiveAnalyticsEngine()
analytics.add_data_point("temp", 72.5)
predictions = analytics.predict_next("temp", steps=5)
```

**See `docs/API_REFERENCE.md` for complete API documentation.**

---

## 📖 Using the Web Interface

### Accessing the System

1. **Start the system:**
   ```bash
   python boot_thalos.py
   ```

2. **Browser opens automatically to:** http://localhost:8000

3. **Experience the Matrix interface:**
   - Animated code rain background
   - Real-time neural activity visualization
   - Interactive chatbot console
   - System status monitoring
   - Live metrics dashboard

### Chatbot Commands

Type these commands in the chat interface:

- `/status` - Full system report with wetware health
- `/metrics` - Neural density, spike rates, lobe activity
- `/lobes` - Detailed organoid lobe analysis
- `/train` - Start adaptive training protocol
- `/help` - Show all available commands

### Natural Conversation

Simply type any question or statement - no commands needed! The system uses:
- Biological neural processing
- Contextual understanding
- Multi-lobe cognitive processing
- Prime Directive ethical framework

### API Access (Optional)

The web interface exposes REST endpoints:

```python
import requests

# Get system status
response = requests.get('http://localhost:8000/api/status')
print(response.json())

# Chat with system
response = requests.post('http://localhost:8000/api/chat',
                        json={'message': 'Hello, Thalos'})
print(response.json()['response'])
```

---

## 🏗️ System Architecture

### Component Overview

```
Thalos Prime v3.0
├── CIS (Central Intelligence System)
│   ├── System orchestration
│   ├── Lifecycle management
│   └── Subsystem coordination
│
├── Wetware Core
│   ├── Organoid Cores (Logic, Abstract, Governance)
│   ├── MEA Interface (20,000 channels)
│   └── Life Support System
│
├── AI/ML Systems
│   ├── Bio Neural Networks (Spiking neurons)
│   ├── Reinforcement Learning (Q-learning)
│   ├── Hebbian Learning (Synaptic plasticity)
│   └── Pattern Recognition
│
├── Database Layer
│   ├── Auto-reconnecting manager
│   ├── Connection pooling
│   └── Multiple backends (SQLite, PostgreSQL, Redis)
│
└── Interfaces
    ├── Web (Matrix-style chatbot)
    ├── CLI (Command line)
    └── API (REST endpoints)
```

### Wetware Components

**Organoid Cores** - Simulated brain tissue:
- Logic Lobe: Reasoning and code generation
- Abstract Lobe: Creative synthesis and innovation
- Governance Lobe: Ethical evaluation and Prime Directive enforcement

**MEA Interface** - Neural communication:
- 20,000 electrode channels
- Signal translation (digital ↔ biological)
- Spike sorting and pattern detection

**Life Support** - Biological homeostasis:
- Temperature: 36.5-37.5°C
- pH: 7.2-7.6
- O₂ saturation: >90%
- Glucose: 3.0-7.0 mM

### AI Systems

**Bio Neural Network:**
- Leaky Integrate-and-Fire neuron model
- STDP learning (strengthens active synapses)
- Homeostatic regulation
- Configurable layers and connectivity

**Reinforcement Learning:**
- Q-learning with experience replay
- Dopamine-like reward signals
- Epsilon-greedy exploration
- Policy and value functions

---

## 🔧 Configuration

### Environment Setup

Create a `.env` file from the template:

```bash
cp .env.example .env
```

**Key settings for web deployment:**

```env
# Production Mode
THALOS_ENV=production
THALOS_DEBUG=false
FLASK_ENV=production

# Web Server
THALOS_API_HOST=0.0.0.0
THALOS_API_PORT=8000

# Storage (Choose one)
THALOS_STORAGE_TYPE=file  # Recommended
THALOS_STORAGE_PATH=/app/data/storage.json

# Security (CHANGE THESE!)
THALOS_SECRET_KEY=your-secure-random-key-here
THALOS_API_KEY=your-api-key-here
```

**Generate secure keys:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Storage Options

| Type | Best For | Setup Required |
|------|----------|----------------|
| `memory` | Development, testing | None |
| `file` | Small-medium deployments | None |
| `redis` | High-performance, scaling | Redis server |
| `postgresql` | Enterprise, large-scale | PostgreSQL |

### Network Configuration

**Local access only:**
```bash
python thalos_prime.py web --host 127.0.0.1 --port 8000
```

**Network-wide access:**
```bash
python thalos_prime.py web --host 0.0.0.0 --port 8000
```

**Custom port:**
```bash
python thalos_prime.py web --port 8080
```

---

## 🐳 Docker Deployment

**Production-ready containerized deployment:**

### Quick Start

```bash
docker-compose up
```

Access at: **http://localhost:8000**

### Manual Docker

```bash
# Build image
docker build -t thalos-prime:3.0 .

# Run container
docker run -d \
  --name thalos-prime \
  -p 8000:8000 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  thalos-prime:3.0
```

### Docker with Custom Configuration

```bash
docker run -d \
  --name thalos-prime \
  -p 8000:8000 \
  -e THALOS_ENV=production \
  -e THALOS_STORAGE_TYPE=file \
  -e THALOS_STORAGE_PATH=/app/data/storage.json \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  thalos-prime:3.0
```

### Cloud Deployment

**AWS, Azure, GCP ready!** See [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md) for:
- AWS ECS/EC2 deployment
- Azure Container Instances
- Google Cloud Run
- Kubernetes configurations
- SSL/HTTPS setup
- Production best practices

---

## 🧪 Testing

```bash
# Quick system test
python test_system.py

# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Test specific component
python tests/unit/test_memory.py

# With coverage
pytest --cov=src tests/
```

---

## 📚 Documentation

- **[WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md)** - Complete web deployment documentation
- **[SETUP.md](SETUP.md)** - Detailed installation and setup
- **[AUTO_WEB_DEPLOY_IMPLEMENTATION.md](AUTO_WEB_DEPLOY_IMPLEMENTATION.md)** - Auto-deployment features
- **[DEPLOYMENT_COMPLETE.md](DEPLOYMENT_COMPLETE.md)** - Deployment status and notes
- **[docs/](docs/)** - Architecture and API documentation

---

## 🎯 Key Features

✅ **Web-First Architecture** - Immersive browser-based interface  
✅ **Matrix-Style UI** - Code rain with neural visualization  
✅ **One-Command Deployment** - Launch in seconds  
✅ **Biological Computation** - Brain organoid simulation with STDP  
✅ **20,000 Channel MEA** - Multi-electrode array interface  
✅ **Life Support** - Temperature, pH, O₂, glucose regulation  
✅ **Spiking Neural Networks** - Leaky integrate-and-fire neurons  
✅ **Reinforcement Learning** - Q-learning with dopamine modulation  
✅ **Auto-Reconnecting Database** - Resilient data persistence  
✅ **Docker Support** - Production-ready containerization  
✅ **REST API** - Programmatic access  
✅ **Cloud Ready** - AWS, Azure, GCP compatible  
✅ **SSL/HTTPS Ready** - Production security  
✅ **Comprehensive Tests** - Unit and integration testing  

---

## 🔒 Security & Production

**For production web deployment:**

1. **Change default secrets:**
   ```bash
   THALOS_SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
   THALOS_API_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
   ```

2. **Use HTTPS:**
   - Set up nginx/traefik as reverse proxy
   - Enable SSL/TLS certificates (Let's Encrypt)
   - Configure HTTPS redirects

3. **Configure storage:**
   - Use file-based or database storage (not memory)
   - Enable automated backups
   - Set up connection pooling

4. **Firewall & Network:**
   - Configure firewall rules (allow port 8000 or 443)
   - Use private networks for database connections
   - Enable DDoS protection (Cloudflare)

5. **Monitoring:**
   - Set up health check monitoring
   - Enable logging to files
   - Configure alerts for failures

**See [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md) for complete security checklist.**

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

---

## 📄 License

© 2026 Tony Ray Macier III. All rights reserved.

Thalos Prime is a proprietary system. Unauthorized reproduction, modification, distribution, or use is strictly prohibited without express written permission.

See [THALOS-PRIME-LICENSE.txt](THALOS-PRIME-LICENSE.txt) for full license details.

---

## 🆘 Support & Troubleshooting

### Common Issues

**Web server won't start:**
```bash
# Check if port is in use
lsof -i :8000

# Try different port
python thalos_prime.py web --port 8080

# Reinstall dependencies
pip install -r requirements.txt
```

**Browser doesn't open automatically:**
- Manually navigate to: http://localhost:8000
- Check firewall settings
- Try different browser

**"Module not found" errors:**
```bash
pip install -r requirements.txt
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
```

**Docker issues:**
```bash
# Rebuild without cache
docker build --no-cache -t thalos-prime:3.0 .

# Check logs
docker logs thalos-prime

# Check health
docker ps
```

**Database connection fails:**
```bash
# Use file-based storage
export THALOS_STORAGE_TYPE=file
python boot_thalos.py
```

### Getting Help

1. Check health status: http://localhost:8000/api/status
2. Review logs in `logs/` directory
3. Run diagnostics: `python test_system.py`
4. See [WEB_DEPLOYMENT_GUIDE.md](WEB_DEPLOYMENT_GUIDE.md)
5. Open GitHub issue with logs and error details

---

## 🎉 Success Indicators

You know Thalos Prime is working when you see:

✓ Browser auto-opens to http://localhost:8000  
✓ Matrix code rain animation playing  
✓ System status: "OPERATIONAL"  
✓ Neural visualization active  
✓ Chat interface responsive  
✓ Organoid lobes showing activity  
✓ Database connections healthy  

---

**THALOS PRIME v3.0**  
*The future of intelligence is biological.*

**Status:** WEB DEPLOYMENT READY  
**Interface:** MATRIX IMMERSIVE  
**Mode:** PRODUCTION OPTIMIZED  
**Prime Directive:** ACTIVE
