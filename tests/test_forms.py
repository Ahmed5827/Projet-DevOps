import pytest
from app.forms import LoginForm, RegistrationForm, TicketForm, CommentForm
from app.models import User


def test_login_form_validation(app):
    """Test login form validation."""
    with app.app_context():
        # Valid form data
        form = LoginForm(username='testuser', password='password')
        assert form.validate() is True
        
        # Invalid - missing username
        form = LoginForm(password='password')
        assert form.validate() is False
        
        # Invalid - missing password
        form = LoginForm(username='testuser')
        assert form.validate() is False


def test_registration_form_validation(app):
    """Test registration form validation."""
    with app.app_context():
        # Valid form data
        form = RegistrationForm(
            username='newuser',
            email='newuser@example.com',
            password='password',
            password2='password'
        )
        assert form.validate() is True
        
        # Invalid - username too short
        form = RegistrationForm(
            username='a',  # Too short
            email='newuser@example.com',
            password='password',
            password2='password'
        )
        assert form.validate() is False
        
        # Invalid - passwords don't match
        form = RegistrationForm(
            username='newuser',
            email='newuser@example.com',
            password='password',
            password2='different'
        )
        assert form.validate() is False
        
        # Invalid - username already exists
        form = RegistrationForm(
            username='testuser',  # Already exists in test database
            email='newuser@example.com',
            password='password',
            password2='password'
        )
        assert form.validate() is False
        
        # Invalid - email already exists
        form = RegistrationForm(
            username='newuser',
            email='user@example.com',  # Already exists in test database
            password='password',
            password2='password'
        )
        assert form.validate() is False


def test_ticket_form_validation(app):
    """Test ticket form validation."""
    with app.app_context():
        # Valid form data
        form = TicketForm(
            title='Test Ticket',
            description='This is a test ticket',
            priority='high'
        )
        assert form.validate() is True
        
        # Invalid - missing title
        form = TicketForm(
            description='This is a test ticket',
            priority='high'
        )
        assert form.validate() is False
        
        # Invalid - missing description
        form = TicketForm(
            title='Test Ticket',
            priority='high'
        )
        assert form.validate() is False
        
        # Invalid - invalid priority
        form = TicketForm(
            title='Test Ticket',
            description='This is a test ticket',
            priority='invalid'  # Not in choices
        )
        assert form.validate() is False


def test_comment_form_validation(app):
    """Test comment form validation."""
    with app.app_context():
        # Valid form data
        form = CommentForm(content='This is a test comment')
        assert form.validate() is True
        
        # Invalid - missing content
        form = CommentForm()
        assert form.validate() is False
