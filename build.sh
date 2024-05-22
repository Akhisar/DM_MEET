#!/bin/bash

# Define a timestamp function for unique tag
timestamp() {
  date +"%Y%m%d%H%M%S"
}

# Define image name and tag
IMAGE_NAME="metric_api_app"
TAG=$(timestamp)

# Build the Docker image
docker build -t ${IMAGE_NAME}:${TAG} .

docker image tag ${IMAGE_NAME}:${TAG}  ${IMAGE_NAME}:latest

# Run the Docker container
#docker run -p 8080:80 -d ${IMAGE_NAME}:${TAG}

#docker stop ${IMAGE_NAME}:${TAG}; docker rm ${IMAGE_NAME}:${TAG}