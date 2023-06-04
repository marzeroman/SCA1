# Use the base image with Python 3.9
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY main.py calculator.py /app/

# Set the entrypoint command to run the main.py script
CMD ["python3", "main.py", "5", "10", "15"]
