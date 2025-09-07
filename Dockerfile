# -------------------------------
# Stage 1: Build Python dependencies
# -------------------------------
FROM python:3.11-slim as builder

WORKDIR /app

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
FROM python:3.11-slim

# Install Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy project
COPY . .

# Collect static files (run at build time)
RUN python app/manage.py collectstatic --noinput

# Copy Nginx config
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose ports (Nginx runs on 80)
EXPOSE 80

# Start script (runs Gunicorn + Nginx)
CMD service nginx start && \
    gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 4 --timeout 120
