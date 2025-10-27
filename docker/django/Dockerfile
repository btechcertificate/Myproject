# -------------------------------
# Stage 1: Build Python dependencies
# -------------------------------
FROM python:3.11-slim as builder

WORKDIR /myprojectdir

# System dependencies
RUN apt-get update && apt-get install -y \
    gcc libpq-dev python3-dev musl-dev && rm -rf /var/lib/apt/lists/*

# Install Python deps in a virtual environment
COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

    
# -------------------------------
# Stage 2: Final image with Nginx + Gunicorn
# -------------------------------
# FROM python:3.11-slim

# # Install Nginx
# RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# WORKDIR /myprojectdir

# # Copy virtualenv from builder
# COPY --from=builder /opt/venv /opt/venv
# ENV PATH="/opt/venv/bin:$PATH"

# Copy project
COPY . .

# Copy entrypoint
COPY docker/django/entrypoint.sh /entrypoint.sh

# Giving permissions to the entrypoint script
RUN chmod +x /entrypoint.sh

# Use entrypoint (In this script, we start both Gunicorn and Nginx and also loading static files)
ENTRYPOINT ["/entrypoint.sh"]
