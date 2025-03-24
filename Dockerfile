# Use a lightweight Python base image
FROM python:3.9-slim

# Create and set the working directory
WORKDIR /app

# Install system dependencies if needed (e.g., libpq-dev for PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your application code
COPY . /app/

# Expose port 8000 (the port your Django app listens on)
EXPOSE 8000

# Use Gunicorn as your production server
# Make sure to replace 'inventory_management.wsgi' with your actual project WSGI module
CMD ["gunicorn", "inventory_management.wsgi:application", "--bind", "0.0.0.0:8000"]
