terraform {
  required_providers {
    null = {
      source  = "hashicorp/null"
      version = "~> 3.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

# Windows-specific Docker deployment using local-exec provisioners
# This approach uses triggers to make terraform plan work without Docker connectivity

# Create a local file to store deployment information
resource "local_file" "deployment_info" {
  content  = "Deployment timestamp: ${timestamp()}"
  filename = "${path.module}/deployment_info.txt"
}

# Create a Docker instructions file for Windows users
resource "local_file" "docker_instructions" {
  content  = <<-EOT
    # Docker Setup Instructions for Windows

    If you're seeing Docker connectivity errors, follow these steps:

    1. Make sure Docker Desktop is installed
       - Download from https://www.docker.com/products/docker-desktop/

    2. Start Docker Desktop
       - Look for Docker Desktop in your Start menu
       - Wait for it to fully initialize (you should see the Docker icon in your system tray)

    3. Check Docker settings
       - Right-click on the Docker Desktop icon in the system tray
       - Select "Settings"
       - Under "General", make sure "Use the WSL 2 based engine" is properly configured
       - Under "Resources", make sure you have allocated enough memory

    4. Restart Docker Desktop if needed
       - Right-click on the Docker Desktop icon in the system tray
       - Select "Restart"

    5. Run Terraform commands again
       - terraform init
       - terraform plan
       - terraform apply

    For more help, visit: https://docs.docker.com/desktop/troubleshoot/overview/
  EOT
  filename = "${path.module}/docker_instructions.md"
}

# Docker deployment resource with triggers
resource "null_resource" "docker_deployment" {
  # Use triggers to control when this resource needs to be recreated
  # This allows terraform plan to work without Docker connectivity
  triggers = {
    deployment_info = local_file.deployment_info.content
  }

  # Deploy the Docker container when terraform apply is run
  provisioner "local-exec" {
    # Windows PowerShell script to check Docker, build and run the container
    command = <<-EOT
      # Check if Docker is running
      Write-Host "Checking Docker connectivity..."
      $dockerRunning = $false
      try {
        $dockerInfo = docker info 2>&1
        if ($LASTEXITCODE -eq 0) {
          $dockerRunning = $true
          Write-Host "Docker is running properly."
        } else {
          Write-Host "Docker is not running properly."
          Write-Host "ERROR: Docker Desktop is not running correctly on your Windows machine."
          Write-Host "Please check the instructions in the docker_instructions.md file."
          Write-Host "Common issues:"
          Write-Host "1. Docker Desktop is not started"
          Write-Host "2. Docker Desktop is still initializing"
          Write-Host "3. Docker Desktop needs to be run as Administrator"
          exit 1
        }
      } catch {
        Write-Host "Error checking Docker: $_"
        Write-Host "Please check the instructions in the docker_instructions.md file."
        exit 1
      }

      # Build the Docker image
      Write-Host "Building Docker image..."
      try {
        docker build -t ticket-management-system-projet-devops:latest ..
        if ($LASTEXITCODE -ne 0) {
          Write-Host "ERROR: Failed to build Docker image."
          exit 1
        }
      } catch {
        Write-Host "Error building Docker image: $_"
        exit 1
      }

      # Remove existing container if it exists
      Write-Host "Removing existing container if it exists..."
      docker rm -f ticket-management-system-projet-devops 2>$null

      # Run the new container
      Write-Host "Starting container..."
      try {
        docker run -d -p 5000:5000 --name ticket-management-system-projet-devops ticket-management-system-projet-devops:latest
        if ($LASTEXITCODE -ne 0) {
          Write-Host "ERROR: Failed to start Docker container."
          exit 1
        }
      } catch {
        Write-Host "Error starting Docker container: $_"
        exit 1
      }

      Write-Host "Docker deployment completed successfully."
      Write-Host "Your application should be running at: http://localhost:5000"
    EOT
    interpreter = ["PowerShell", "-Command"]
    on_failure  = continue
  }

  # Clean up when terraform destroy is run
  provisioner "local-exec" {
    when = destroy
    command = <<-EOT
      Write-Host "Cleaning up Docker resources..."
      docker stop ticket-management-system-projet-devops 2>$null
      docker rm ticket-management-system-projet-devops 2>$null
      Write-Host "Cleanup completed."
    EOT
    interpreter = ["PowerShell", "-Command"]
    on_failure  = continue
  }
}
