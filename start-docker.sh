#!/bin/bash

# Start Docker daemon
dockerd &

# Wait for Docker to start
while ! docker info >/dev/null 2>&1; do
  echo "Waiting for Docker to start..."
  sleep 1
done

echo "Docker started successfully."