# Terraform Setup for CI/CD Pipeline

This document explains how the Terraform deployment is configured in the CI/CD pipeline.

## Overview

The CI/CD pipeline uses Terraform to deploy the application as a Docker container. The workflow:

1. Runs tests on the Python code
2. Sets up Terraform and Docker
3. Creates a Terraform configuration that builds a Docker image from the application code
4. Deploys a Docker container running the application

## Terraform Configuration

The Terraform configuration created by the workflow does the following:

1. Uses the Docker provider to interact with Docker
2. Builds a Docker image from the application code
3. Creates a Docker container from the image
4. Exposes the application on port 5000

## Requirements

To run this workflow successfully:

1. The GitHub Actions runner must have Docker installed
2. The runner must have permission to build Docker images and run containers

## Local Testing

You can test the Terraform configuration locally by:

1. Creating the `infra` directory: `mkdir -p infra`
2. Creating the `main.tf` file with the following content:

```hcl
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "myapp" {
  name = "myapp"
  build {
    context = "${path.module}/.."
  }
}

resource "docker_container" "myapp" {
  name = "myapp"
  image = docker_image.myapp.latest

  ports {
    internal = 5000
    external = 5000
  }
}
```

3. Running Terraform commands:
   ```
   terraform init
   terraform plan
   terraform apply
   ```

## Customizing the Configuration

You can customize the Terraform configuration by:

1. Modifying the container name, port mappings, or other settings
2. Adding environment variables to the container
3. Adding volume mounts for persistent data
4. Configuring container networking

## Notes

- The Docker image is built from the application code in the repository
- The container exposes the application on port 5000
- No external secrets or credentials are required for this configuration
