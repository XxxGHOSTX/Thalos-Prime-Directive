# Thalos Prime v3.0 - Docker Container (Web Deployment)
# Multi-stage build for optimized web deployment

# Build stage
FROM python:3.12-slim as builder

WORKDIR /build

# Copy dependency file first for better caching
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy source files
COPY src/ ./src/
COPY tests/ ./tests/
COPY config/ ./config/
COPY create_thalos_bootstrap.sh ./

# Verify build
RUN python -m py_compile src/**/*.py && \
    chmod +x create_thalos_bootstrap.sh

# Production stage
FROM python:3.12-slim

LABEL maintainer="Thalos Prime Team"
LABEL version="3.0"
LABEL description="Thalos Prime - Synthetic Biological Intelligence System (Web Deployment)"

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy from builder
COPY --from=builder /build/src ./src
COPY --from=builder /build/config ./config
COPY --from=builder /build/create_thalos_bootstrap.sh ./

# Create directories
RUN mkdir -p /app/docs /app/tests /app/data /app/logs

# Set Python path and add local packages to PATH
ENV PYTHONPATH=/app/src
ENV PATH=/root/.local/bin:$PATH

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/api/status || exit 1

# Default command - Start web interface
CMD ["python", "-u", "/app/src/interfaces/web/immersive_server.py"]

# Expose web interface port
EXPOSE 8000

# Volume for persistence (optional)
VOLUME ["/app/data"]
