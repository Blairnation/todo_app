# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your app code to the container
COPY . /app/

# Expose the application port
EXPOSE 8000

# Start the Django server using Gunicorn
CMD ["gunicorn", "base.wsgi:application", "--bind", "0.0.0.0:8000"]
