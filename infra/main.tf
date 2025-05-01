terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

# Use a local-exec provisioner to build the Docker image directly
resource "null_resource" "docker_build" {
  provisioner "local-exec" {
    command = "docker build -t ticket-management-system-projet-devops:latest .."
  }
}

# Use the pre-built image instead of building it with Terraform
resource "docker_image" "ticket-management-system-projet-devops" {
  name = "ticket-management-system-projet-devops:latest"
  depends_on = [null_resource.docker_build]
}

resource "docker_container" "ticket-management-system-projet-devops" {
  name  = "ticket-management-system-projet-devops"
  image = docker_image.ticket-management-system-projet-devops.image_id

  ports {
    internal = 5000
    external = 5000
  }
}
