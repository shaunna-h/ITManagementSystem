# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory in the container
WORKDIR /ITManagementSystem

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt /ITManagementSystem/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code into the container
COPY . /ITManagementSystem/

# # Collect static files (if applicable)
# RUN python manage.py collectstatic --noinput

# Expose the port the app runs on (adjust if needed)
EXPOSE 8000

# Use Gunicorn as the WSGI HTTP Server (adjust the number of workers as necessary)
CMD ["gunicorn", "inventory_management.wsgi:application", "--bind", "127.0.0.1:8000"]
