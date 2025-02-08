from api import create_app, db  # Import the create_app function and db instance
from api.config import DevelopmentConfig  # Import configuration settings
from api.models import User, UserProfile, UserMembership
from werkzeug.security import generate_password_hash

# Create the Flask app instance by calling the create_app function
app = create_app(config_class=DevelopmentConfig)

with app.app_context():
    db.create_all()
    # Optionally, add a dummy user if none exists.
    if not User.query.first():
        password=generate_password_hash('password')
        user = User(username='testuser', email='test@test.com', password=password)
        profile = UserProfile(first_name='Test', last_name='User', user=user)
        # Associate membership with the profile, not the user.
        membership = UserMembership(user_profile=profile, membership_type='customer', submembership_type='basic')
        db.session.add(user)
        db.session.add(profile)
        db.session.add(membership)
        db.session.commit()
        print('Dummy user created.')

if __name__ == '__main__':
    app.run(debug=True)
