# Helpdesk Ticket Management System

### 🌐🔗 [Live Demo](https://ticket-management-system-projet-devops.onrender.com/) 🔗🌐
#

A full-featured helpdesk ticket management system built with Flask. This application allows users to create, view, update, and manage support tickets with different priority levels. It includes user authentication, role-based access control, and a responsive UI.

![Helpdesk Screenshot](https://lh3.googleusercontent.com/fife/ALs6j_GBF3YZW4dU7V0VyfB9DuDBZR0Od07D0q68ssWDsH7Ih853ySR-50csU1ENWOjm-VIUBIkr8ku_VavxjQ3M0Cmddy35m4Vceqg5XKBe1rBhD1_wfrHfU5Y8bTflEZM6DxNqkm2y8WKLPkxWHu0Hxsh7hb1_9wuzDRBQTdKaOQoHc79LBJJ2Cn6sgkJGh2LvV5IrQBY_piHNzo3acHKpC9p0FoonlI5gSna9VmWbCmocHdkwT6-2F8LL9ap6GY21GDikNoLcwwG0L5h9diHTRZkJGswr_9gZGQ3LTTHdfFSeZv2LSmyVoL1GyahdORlk8-0yKaExAztDP2k4aDeIhyYbTe4sjErvxfWnkFEKEiu_9rNrnGYsQK0Ze7UdZDBP8vUIj3nfIhE2q0rMx4F8au4lbQeszR2Qye9pt6aEg3EIHu8Hc0W0jz2fqofsbkqNf-15VbTkYDAwK6huaWFYEZljuDLjGSdXp-Y0LQU342oR3ARJW-yyEXmf-6DlER4yoUfOQVBDPmR8vlxMjFn0KYiWPPsG6GLmyqf54jgR6BQuynLNbOiRAixP_TA90l_w-LXEFhFQyU_MXTAcVahSgbpUJxrIbC6JHbJTkrUpQdihrfhSJKKvpVv-MwcgoYko5Nt_sb_7XJa6nlU3BxVG-Bg76YynOYjUHw2rXQJMpcSSM17AclekiWxcmsTBdMpzxNe3fxwXLWPP1LCeIycST0GnIQTZU6q-jckQ7cHoE2hL4gwezPD5Ke-12BUAvBAijtwWwTLa49USAZx1WN0keKdPF4qr0fmWMED87AgUf9UVPgwP5Q6AMGgtxpAQ7biGnb3DXVGNab5XwiEBAIh4NkRVAcHptcks1Y3R4sVMLlh8VC25ifIch6LYqIPZ5QRHu5qcWSUbmlGPVAsbydfpTifo6Tu5nR7_y8erfU_pyVWramWtfGRHyMHzqw2jpxAHAVd0gwgs2ngPwN2N3rXTYifRq9NPc6pDIAAEu154lJkY0CFOR_BfCTFP4fgsLCznVhsWnEbCxYIk95AL7eINReqVPwR-cJLwDltLrWFfh2RO2YuQzU_flwospaY_bFjb2pHj7y-mP8Qi3RALxz4JKotDtxWuHy_hpagUjxYjXsfrzE2DBEjFxt5FCwwgh1gL2dxKEcr6fLp1NzMOZdhjIbbVkaIHj7oGbet_NeLvDl5iLfmHs5R6G23nXLKSwBrpaofqEu7-z2i1BBSUy1bBoBvuONO5ZU9AqVulSx5vDN3gTVUJBb90i0ec03p85YbQunAKYJGSsjy3-cUkw5YRgU0YlhiU-h3001ZrvXkRg4UaJDcMFhI1va8M4-TEwDSjmuvURM4RiBXwoLfeIDqZA2BBWGaa7u9cpRaH6Rhx4rLCf-sUJ2bKbJOyL_dBGNapdE8bZ25COVHeuDt-GtThL_P2h9BaiXGOZVrvntl-3qbI_9AC7GrvlOn2qzjPYnqYwkt0RhET5dcbpugmsr8uHv4chq4vzorzwWX9K7oP1onfuDiXE_WPuNKqjqWcnf3jzoJ_-kIyef5avhPJQlBDBNc3JDYFr_qFId0mheo7DcIryXCpRPxNhF7Tvw--4z6fPMngd2OctSAw0SuMuQInrOWnANNqJ4Zgusmmd8JaAowN5HLnrLu_STc5mvPkoiFbjih5WcsZhHJOCOfIqeQ3nvy64MLnCmk6pewlC78nBxwCe7UxBGAQPYEihaZMvFY2wk3N5wNdZQkLM09AUKHGCkKMvIK7ABhMDjZfyPkVhglj-dcPxCERJGHAiR7xSS1aTSIFLXZwh5c=w1878-h964?auditContext=forDisplay)

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
