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
