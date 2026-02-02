# Thalos Prime v3.0 - Web Deployment Guide

**© 2026 Tony Ray Macier III. All rights reserved.**

---

## Overview

Thalos Prime v3.0 is now optimized as a **web-based deployment only** system, providing an immersive Matrix-style interface to the Synthetic Biological Intelligence System.

## Quick Start (Recommended)

### Single Command Deployment

The fastest way to get Thalos Prime running:

**Linux/macOS:**
```bash
./start_web.sh
```

**Windows:**
```cmd
start_web.bat
```

**Universal (All platforms):**
```bash
python boot_thalos.py
```

This will:
- ✅ Check Python installation (3.12+ required)
- ✅ Install all dependencies automatically
- ✅ Create necessary directories (data, logs)
- ✅ Configure environment (.env from template)
- ✅ Start web server on http://localhost:8000
- ✅ Auto-launch browser to the interface

**Expected result:** Browser opens to an immersive Matrix-style interface with:
- Animated code rain background
- Real-time neural activity visualization
- Interactive chatbot console
- System status monitoring
- Live metrics dashboard

---

## Deployment Options

### Option 1: Direct Python Launch (Fastest)

```bash
python boot_thalos.py
```

Best for:
- Quick testing and development
- Local deployment
- First-time users
- Demo purposes

### Option 2: Production Python Mode

```bash
python thalos_prime.py web
```

Or with custom configuration:
```bash
python thalos_prime.py web --host 0.0.0.0 --port 8080
```

Best for:
- Custom port configuration
- Network-accessible deployments
- Advanced users

### Option 3: Docker Deployment (Production)

**Quick Start:**
```bash
docker-compose up
```

**Manual Docker:**
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

Best for:
- Production deployments
- Cloud hosting (AWS, Azure, GCP)
- Scalable infrastructure
- Enterprise environments

### Option 4: Production with Gunicorn

For high-performance production deployments:

```bash
# Install gunicorn
pip install gunicorn

# Run with multiple workers
gunicorn -w 4 -b 0.0.0.0:8000 "src.interfaces.web.immersive_server:app"
```

Best for:
- High-traffic deployments
- Load-balanced environments
- Multi-core server optimization

---

## Configuration

### Environment Variables

Create a `.env` file from the template:

```bash
cp .env.example .env
```

**Key Configuration Options:**

```env
# Production Settings
THALOS_ENV=production
THALOS_DEBUG=false

# Web Server
THALOS_API_HOST=0.0.0.0
THALOS_API_PORT=8000
FLASK_ENV=production

# Storage (Choose one)
THALOS_STORAGE_TYPE=file  # Recommended for production
THALOS_STORAGE_PATH=/app/data/storage.json

# Security (CHANGE THESE!)
THALOS_SECRET_KEY=generate-secure-random-key-here
THALOS_API_KEY=generate-secure-api-key-here
```

**Generate Secure Keys:**
```bash
# For SECRET_KEY
openssl rand -hex 32

# For API_KEY
openssl rand -hex 32
```

### Storage Options

**1. Memory (Default - Development Only)**
```env
THALOS_STORAGE_TYPE=memory
```
- ⚠️ Data lost on restart
- ✅ No setup required
- ✅ Fast

**2. File-Based (Recommended for Small/Medium Deployments)**
```env
THALOS_STORAGE_TYPE=file
THALOS_STORAGE_PATH=/app/data/storage.json
```
- ✅ Persistent storage
- ✅ No external dependencies
- ⚠️ Not suitable for high concurrency

**3. Redis (High Performance)**
```env
THALOS_STORAGE_TYPE=redis
THALOS_REDIS_URL=redis://localhost:6379/0
```
- ✅ High performance
- ✅ Distributed caching
- ⚠️ Requires Redis server

**4. PostgreSQL (Enterprise)**
```env
THALOS_STORAGE_TYPE=postgresql
THALOS_DATABASE_URL=postgresql://user:pass@localhost/thalos
```
- ✅ Enterprise-grade
- ✅ ACID compliance
- ✅ Best for large-scale deployments
- ⚠️ Requires PostgreSQL server

---

## Network Access

### Local Access Only (Development)
```bash
python thalos_prime.py web --host 127.0.0.1 --port 8000
```
Access: http://localhost:8000

### Network-Wide Access (Production)
```bash
python thalos_prime.py web --host 0.0.0.0 --port 8000
```
Access: http://YOUR_SERVER_IP:8000

### Custom Port
```bash
python thalos_prime.py web --port 8080
```
Access: http://localhost:8080

---

## Cloud Deployment

### AWS (Amazon Web Services)

**Using EC2:**
```bash
# On EC2 instance
git clone https://github.com/XxxGHOSTX/Thalos-Prime-Directive.git
cd Thalos-Prime-Directive
./start_web.sh

# Configure security group to allow port 8000
```

**Using ECS (Docker):**
```bash
# Build and push to ECR
docker build -t thalos-prime:3.0 .
docker tag thalos-prime:3.0 YOUR_ECR_URL/thalos-prime:3.0
docker push YOUR_ECR_URL/thalos-prime:3.0

# Deploy via ECS task definition
```

### Azure

**Using Azure Container Instances:**
```bash
az container create \
  --resource-group thalos-rg \
  --name thalos-prime \
  --image thalos-prime:3.0 \
  --ports 8000 \
  --dns-name-label thalos-prime
```

### Google Cloud Platform

**Using Cloud Run:**
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT_ID/thalos-prime
gcloud run deploy thalos-prime \
  --image gcr.io/PROJECT_ID/thalos-prime \
  --platform managed \
  --port 8000
```

### DigitalOcean

**Using Droplet:**
```bash
# On droplet
git clone https://github.com/XxxGHOSTX/Thalos-Prime-Directive.git
cd Thalos-Prime-Directive
./start_web.sh
```

**Using App Platform (Docker):**
- Push Docker image to registry
- Create app from Docker image
- Set port to 8000

---

## SSL/HTTPS Configuration

For production deployments, always use HTTPS:

### Option 1: Nginx Reverse Proxy

**nginx.conf:**
```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Option 2: Traefik Reverse Proxy

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  traefik:
    image: traefik:v2.10
    command:
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=your@email.com"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

  thalos-prime:
    image: thalos-prime:3.0
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.thalos.rule=Host(`your-domain.com`)"
      - "traefik.http.routers.thalos.entrypoints=websecure"
      - "traefik.http.routers.thalos.tls.certresolver=myresolver"
```

---

## Monitoring & Health Checks

### Health Check Endpoint
```bash
curl http://localhost:8000/api/status
```

**Expected Response:**
```json
{
  "cis": {
    "status": "operational",
    "version": "3.0",
    "subsystems": {...}
  },
  "memory_entries": 0,
  "system_health": "OPERATIONAL",
  "version": "3.0.0"
}
```

### Docker Health Check
Built-in health check in Dockerfile:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/api/status || exit 1
```

### Monitoring with Prometheus

**prometheus.yml:**
```yaml
scrape_configs:
  - job_name: 'thalos-prime'
    static_configs:
      - targets: ['localhost:8000']
```

---

## Performance Tuning

### Gunicorn Workers
```bash
# Calculate optimal workers: (2 x CPU cores) + 1
gunicorn -w 9 -b 0.0.0.0:8000 "src.interfaces.web.immersive_server:app"
```

### Resource Limits (Docker)
```yaml
services:
  thalos-prime:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

### Caching with Redis
```env
THALOS_STORAGE_TYPE=redis
THALOS_REDIS_URL=redis://localhost:6379/0
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 8000
lsof -i :8000
# Or use alternative port
python thalos_prime.py web --port 8080
```

### Dependencies Missing
```bash
pip install -r requirements.txt
```

### Permission Denied (Linux/macOS)
```bash
chmod +x start_web.sh
chmod +x boot_thalos.py
```

### Docker Build Fails
```bash
# Clear cache and rebuild
docker build --no-cache -t thalos-prime:3.0 .
```

### Browser Doesn't Auto-Open
Manually navigate to: http://localhost:8000

---

## Security Checklist

For production deployments:

- [ ] Change `THALOS_SECRET_KEY` to random secure value
- [ ] Change `THALOS_API_KEY` to random secure value
- [ ] Set `THALOS_DEBUG=false`
- [ ] Set `THALOS_ENV=production`
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Use strong database credentials
- [ ] Enable security headers in reverse proxy
- [ ] Regular security updates
- [ ] Monitor system logs

---

## System Requirements

### Minimum:
- Python 3.12+
- 2GB RAM
- 1 CPU core
- 500MB disk space

### Recommended:
- Python 3.12+
- 4GB+ RAM
- 2+ CPU cores
- 2GB+ disk space
- SSD storage

### Production:
- Python 3.12+
- 8GB+ RAM
- 4+ CPU cores
- 10GB+ disk space
- SSD storage
- Load balancer
- Redis/PostgreSQL

---

## Support

For issues or questions:
1. Check system status: http://localhost:8000/api/status
2. Review logs in `logs/` directory
3. Run diagnostics: `python test_system.py`
4. Open GitHub issue with logs and error messages

---

**THALOS PRIME v3.0**  
*The future of intelligence is biological.*

**Status:** WEB DEPLOYMENT READY  
**Mode:** PRODUCTION OPTIMIZED  
**Prime Directive:** ACTIVE
