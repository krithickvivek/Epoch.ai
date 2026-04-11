FROM python:3.10-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user (required by HF Spaces)
RUN useradd -m -u 1000 user
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create writable directories for runtime data and persistent storage
RUN mkdir -p /app/data /app/static/uploads /data && \
    chown -R user:user /app /data

USER user

# HF Spaces persistent storage volume
VOLUME /data

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost:7860/health || exit 1

CMD ["uvicorn", "curriculum_flow_env.server:app", "--host", "0.0.0.0", "--port", "7860"]
