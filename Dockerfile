FROM python:3.10-slim

# Install curl for healthcheck and git for pip installs
RUN apt-get update && apt-get install -y --no-install-recommends curl git && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user (required by HF Spaces)
RUN useradd -m -u 1000 user
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create writable directories for runtime data (no /data — triggers HF volume mount)
RUN mkdir -p /app/data /app/static/uploads && \
    chown -R user:user /app

USER user

# Environment variables
ENV WORKERS=2
ENV MAX_CONCURRENT_ENVS=100
ENV PORT=7860
ENV HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD curl -f http://localhost:7860/health || exit 1

# Start the main app — serves both the web UI and all OpenENV API endpoints
# (/predict, /reset, /step, /state, /health, /spec, /ws)
CMD ["uvicorn", "curriculum_flow_env.server:app", "--host", "0.0.0.0", "--port", "7860"]
