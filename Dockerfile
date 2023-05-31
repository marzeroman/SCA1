# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy all the files to the container
COPY . .

# Set the entry point to execute the Python script
CMD ["python", "calculator.py"]
