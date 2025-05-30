# Stage 1: Build stage
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN opentelemetry-bootstrap -a install


# Stage 2: Production stage
FROM python:3.12-slim

ARG SPLUNK_ACCESS_TOKEN
ARG SPLUNK_REALM

# Create a non-root user and set permissions
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Copy installed dependencies from the build stage
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy the application code
COPY --chown=appuser:appuser . .

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 8000

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
ENV DJANGO_SETTINGS_MODULE=djtest.settings

ENV OTEL_SERVICE_NAME=swat-9358
ENV OTEL_RESOURCE_ATTRIBUTES=deployment.environment=test-swat
ENV OTEL_TRACES_EXPORTER=otlp,console
ENV SPLUNK_ACCESS_TOKEN=$SPLUNK_ACCESS_TOKEN
ENV OTEL_EXPORTER_OTLP_TRACES_PROTOCOL=http/protobuf
ENV OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://ingest.$SPLUNK_REALM.signalfx.com/v2/trace/otlp
ENV OTEL_PYTHON_LOG_CORRELATION=true

# Command to run the application
CMD ["opentelemetry-instrument", "gunicorn", "--bind", "0.0.0.0:8000", "--threads", "2", "--workers", "4", "--error-log", "-", "app:app"]
 # gunicorn -b 127.0.0.1:8000 -c gunicorn.config.py --threads 2 --workers 4 app:app
