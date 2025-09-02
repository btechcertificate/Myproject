# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /myproject

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose Django dev port.
EXPOSE 8000

# Start app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
