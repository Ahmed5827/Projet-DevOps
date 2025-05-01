# Helpdesk Ticket Management System

A full-featured helpdesk ticket management system built with Flask. This application allows users to create, view, update, and manage support tickets with different priority levels. It includes user authentication, role-based access control, and a responsive UI.

![Helpdesk Screenshot](https://via.placeholder.com/800x400?text=Helpdesk+Screenshot)

## Features

- **User Authentication**: Secure login and registration system
- **Role-Based Access Control**: Admin and regular user roles with different permissions
- **Ticket Management**:
  - Create new support tickets with title, description, and priority
  - View ticket details and history
  - Update ticket information
  - Add comments to tickets
  - Filter and sort tickets
- **Responsive UI**: Built with Bootstrap for a mobile-friendly experience
- **Flash Notifications**: User-friendly feedback for actions
- **Database**: SQLite database for storing users, tickets, and comments

## Technology Stack

- **Backend**: Python 3.11+ with Flask framework
- **Database**: SQLAlchemy ORM with SQLite
- **Frontend**: HTML, Bootstrap 5
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF and WTForms
- **Testing**: pytest with pytest-flask and pytest-cov
- **CI/CD**: GitHub Actions
- **Containerization**: Docker

## Project Structure

```
helpdesk/
├── app/                    # Application package
│   ├── __init__.py         # App initialization
│   ├── models.py           # Database models
│   ├── forms.py            # Form classes
│   ├── routes/             # Route blueprints
│   │   ├── __init__.py
│   │   ├── auth.py         # Authentication routes
│   │   ├── main.py         # Main routes
│   │   └── tickets.py      # Ticket management routes
│   └── templates/          # Jinja2 templates
│       ├── auth/           # Authentication templates
│       ├── tickets/        # Ticket templates
│       ├── base.html       # Base template
│       └── index.html      # Home page
├── tests/                  # Test package
│   ├── __init__.py
│   ├── conftest.py         # Test fixtures
│   ├── test_models.py      # Model tests
│   ├── test_forms.py       # Form tests
│   └── test_routes.py      # Route tests
├── .github/                # GitHub configuration
│   └── workflows/          # GitHub Actions workflows
│       └── ci-cd.yml       # CI/CD pipeline
├── config.py               # Application configuration
├── config_test.py          # Test configuration
├── run.py                  # Development server script
├── run-docker.py           # Docker server script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── pytest.ini              # pytest configuration
└── README.md               # This file
```

## Installation

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/helpdesk-ticket-system.git
   cd helpdesk-ticket-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   venv\Scripts\activate

   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Access the application at http://localhost:5000

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t helpdesk-app .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 helpdesk-app
   ```

3. Access the application at http://localhost:5000

## Testing

Run the test suite with pytest:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=app tests/ -v
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

1. Runs tests on every push and pull request
2. Builds and tests a Docker image
3. Pushes the Docker image to Docker Hub (on main branch)
4. Deploys the container (on main branch)

## User Roles

### Admin User
- Can view all tickets in the system
- Can edit and delete any ticket
- Can manage user permissions

### Regular User
- Can create new tickets
- Can view and edit their own tickets
- Cannot delete tickets or view other users' tickets

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
