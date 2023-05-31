#!/bin/bash

# Build the Docker image
docker build -t calculator ./docker


# Run the Docker container
docker run -d --name calculator-container -p 8080:8080 calculator
