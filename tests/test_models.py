import pytest
from app.models import User, Ticket, Comment
from app import db


def test_user_model(app):
    """Test User model."""
    with app.app_context():
        # Test user creation
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
        assert user.email == 'user@example.com'
        assert user.is_admin is False
        
        # Test password hashing
        assert user.password_hash is not None
        assert user.check_password('password') is True
        assert user.check_password('wrongpassword') is False


def test_ticket_model(app):
    """Test Ticket model."""
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        
        # Create a test ticket
        ticket = Ticket(
            title='Test Ticket',
            description='This is a test ticket',
            priority='high',
            author=user
        )
        db.session.add(ticket)
        db.session.commit()
        
        # Retrieve the ticket and check its properties
        saved_ticket = Ticket.query.filter_by(title='Test Ticket').first()
        assert saved_ticket is not None
        assert saved_ticket.description == 'This is a test ticket'
        assert saved_ticket.priority == 'high'
        assert saved_ticket.status == 'open'  # Default status
        assert saved_ticket.author.username == 'testuser'


def test_comment_model(app):
    """Test Comment model."""
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        
        # Create a test ticket
        ticket = Ticket(
            title='Ticket with Comment',
            description='This ticket will have a comment',
            priority='medium',
            author=user
        )
        db.session.add(ticket)
        db.session.commit()
        
        # Add a comment to the ticket
        comment = Comment(
            content='This is a test comment',
            author=user,
            ticket=ticket
        )
        db.session.add(comment)
        db.session.commit()
        
        # Retrieve the comment and check its properties
        saved_comment = Comment.query.filter_by(content='This is a test comment').first()
        assert saved_comment is not None
        assert saved_comment.author.username == 'testuser'
        assert saved_comment.ticket.title == 'Ticket with Comment'
        
        # Check the relationship from ticket to comments
        assert len(ticket.comments.all()) == 1
        assert ticket.comments.first().content == 'This is a test comment'
