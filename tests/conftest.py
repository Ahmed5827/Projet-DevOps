import pytest
import os
import tempfile
from app import create_app, db
from app.models import User, Ticket, Comment
from config import Config


class TestConfig(Config):
    """Test configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app(TestConfig)
    
    # Create a temporary database
    with app.app_context():
        db.create_all()
        
        # Create a test admin user
        admin = User(username='admin', email='admin@example.com', is_admin=True)
        admin.set_password('password')
        
        # Create a test regular user
        user = User(username='testuser', email='user@example.com')
        user.set_password('password')
        
        # Add users to the database
        db.session.add_all([admin, user])
        db.session.commit()
        
    yield app
    
    # Clean up
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()


@pytest.fixture
def auth(client):
    """Authentication helper for tests."""
    class AuthActions:
        def login(self, username='testuser', password='password'):
            return client.post(
                '/auth/login',
                data={'username': username, 'password': password},
                follow_redirects=True
            )
            
        def logout(self):
            return client.get('/auth/logout', follow_redirects=True)
    
    return AuthActions()
