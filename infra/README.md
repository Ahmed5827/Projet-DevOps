# Terraform Docker Configuration

This directory contains Terraform configuration to deploy the application as a Docker container.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Terraform](https://www.terraform.io/downloads.html) (version 1.0.0 or later)
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (for Windows/Mac) or Docker Engine (for Linux)

## Configuration Details

The Terraform configuration in this directory:
1. Uses the kreuzwerker/docker provider to interact with Docker
2. Builds a Docker image from the application code
3. Creates a Docker container from that image
4. Exposes the application on port 5000

## Testing the Configuration

Follow these steps to test the Terraform configuration:

### 1. Initialize Terraform

Open a terminal in this directory and run:

```
terraform init
```

This will download the required providers and initialize Terraform.

### 2. Create a Plan

Run the following command to see what changes Terraform will make:

```
terraform plan
```

This will show you the resources that will be created (the Docker image and container).

### 3. Apply the Configuration

Run the following command to create the resources:

```
terraform apply
```

When prompted, type `yes` to confirm the changes.

### 4. Verify the Deployment

After Terraform completes, you can verify that the Docker container is running:

```
docker ps
```

You should see a container named "myapp" running and exposing port 5000.

### 5. Test the Application

Open a web browser and navigate to:

```
http://localhost:5000
```

You should see your application running.

### 6. Clean Up

When you're done testing, you can destroy the resources:

```
terraform destroy
```

When prompted, type `yes` to confirm.

## Troubleshooting

If you encounter issues:

### Docker Connection Issues

If you're on Windows and get an error about connecting to Docker, make sure:
1. Docker Desktop is running
2. The Docker Engine API is enabled
3. You're using the correct host path in the provider configuration

For Windows, the host path should be:
```
host = "npipe:////.//pipe//docker_engine"
```

For Linux/macOS, you can use:
```
host = "unix:///var/run/docker.sock"
```

### Build Context Issues

If the Docker build fails, check that:
1. The `context` path in the Terraform configuration is correct
2. Your application has a valid Dockerfile in the root directory
3. The Dockerfile can be built manually with `docker build`

### Port Conflicts

If port 5000 is already in use, you can modify the `external` port in the Terraform configuration to use a different port.
