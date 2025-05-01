import pytest
from app.models import User, Ticket, Comment
from app import db


def test_home_page_redirect_if_not_logged_in(client):
    """Test that home page redirects to login if user is not logged in."""
    response = client.get('/', follow_redirects=False)
    assert response.status_code == 302
    assert '/auth/login' in response.location


def test_home_page_logged_in(client, auth):
    """Test that home page loads correctly when logged in."""
    auth.login()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to HelpDesk' in response.data
    assert b'Hello, testuser' in response.data


def test_login_page(client):
    """Test login page loads correctly."""
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Login' in response.data


def test_login_functionality(client):
    """Test login functionality."""
    # Valid login
    # response = client.post(
    #     '/auth/login',
    #     data={'username': 'ahmed', 'password': '1234dd'},
    #     follow_redirects=True
    # )
    # assert response.status_code == 200
    # assert b'You have been logged in successfully' in response.data

    # Invalid login - wrong password
    response = client.post(
        '/auth/login',
        data={'username': 'ahmed', 'password': 'wrongpassword'},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'HelpDesk - Login' in response.data

    # Invalid login - user doesn't exist
    response = client.post(
        '/auth/login',
        data={'username': 'nonexistentuser', 'password': 'password'},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'HelpDesk - Login' in response.data


def test_logout(client, auth):
    """Test logout functionality."""
    auth.login()
    response = auth.logout()
    assert response.status_code == 200
    assert b'You have been logged out' in response.data


def test_register_page(client):
    """Test register page loads correctly."""
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Register' in response.data


def test_register_functionality(client, app):
    """Test registration functionality."""
    # Valid registration
    response = client.post(
        '/auth/register',
        data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'password2': 'password'
        },
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Registration successful' in response.data

    # Check that user was created in database
    with app.app_context():
        user = User.query.filter_by(username='newuser').first()
        assert user is not None
        assert user.email == 'newuser@example.com'


def test_tickets_page_requires_login(client):
    """Test that tickets page requires login."""
    response = client.get('/tickets', follow_redirects=False)
    assert response.status_code == 302
    assert '/auth/login' in response.location


def test_tickets_page_logged_in(client, auth):
    """Test that tickets page loads correctly when logged in."""
    auth.login()
    response = client.get('/tickets')
    assert response.status_code == 200
    assert b'Help Desk Tickets' in response.data


def test_create_ticket(client, auth, app):
    """Test ticket creation."""
    auth.login()

    # Get the create ticket page
    response = client.get('/tickets/create')
    assert response.status_code == 200
    assert b'Submit Ticket' in response.data

    # Create a ticket
    response = client.post(
        '/tickets/create',
        data={
            'title': 'New Test Ticket',
            'description': 'This is a test ticket created during testing',
            'priority': 'high'
        },
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b'Ticket has been created' in response.data

    # Check that ticket was created in database
    with app.app_context():
        ticket = Ticket.query.filter_by(title='New Test Ticket').first()
        assert ticket is not None
        assert ticket.description == 'This is a test ticket created during testing'
        assert ticket.priority == 'high'
        assert ticket.author.username == 'testuser'


def test_view_ticket(client, auth, app):
    """Test viewing a ticket."""
    # Create a ticket first
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        ticket = Ticket(
            title='Ticket to View',
            description='This ticket will be viewed in a test',
            priority='medium',
            author=user
        )
        db.session.add(ticket)
        db.session.commit()
        ticket_id = ticket.id

    # Login and view the ticket
    auth.login()
    response = client.get(f'/tickets/{ticket_id}')
    assert response.status_code == 200
    assert b'Ticket to View' in response.data
    assert b'This ticket will be viewed in a test' in response.data


def test_add_comment(client, auth, app):
    """Test adding a comment to a ticket."""
    # Create a ticket first
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        ticket = Ticket(
            title='Ticket for Comment',
            description='This ticket will receive a comment',
            priority='low',
            author=user
        )
        db.session.add(ticket)
        db.session.commit()
        ticket_id = ticket.id

    # Login and add a comment
    auth.login()
    response = client.post(
        f'/tickets/{ticket_id}/comment',
        data={'content': 'This is a test comment added during testing'},
        follow_redirects=True
    )
    assert response.status_code == 200

    # Check that comment was added to the database
    with app.app_context():
        comment = Comment.query.filter_by(
            content='This is a test comment added during testing').first()
        assert comment is not None
        assert comment.author.username == 'testuser'
        assert comment.ticket.title == 'Ticket for Comment'
