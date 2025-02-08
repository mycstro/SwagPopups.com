import logging
from datetime import datetime

from flask import (
    flash, Blueprint, render_template, request,
    session, redirect, url_for, jsonify, send_file
)
from flask_restful import Api
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError

# ReportLab imports for PDF generation
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

from .forms import RegistrationForm, ProfileForm, LoginForm
from .models import db, User, UserProfile, UserMembership
from api.config import DevelopmentConfig

# Create a Blueprint
main = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

# Import all the Resource classes from api_resources
from .api_resources import (
    Hello, Square, apiLogin, apiRegister, getSubmembershipTypes
)

# Mock users (optional; remove if not needed)
mock_users = DevelopmentConfig.MOCK_USERS

# ---------------------------------------------------------------------
# After-request handler for logging
# ---------------------------------------------------------------------
@main.after_request
def after_request(response):
    logger.debug(
        f"Response status: {response.status} | "
        f"URL: {request.path} | IP: {request.remote_addr}"
    )
    return response

# ---------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------
@main.route('/')
def home():
    """ Home page route """
    user_ip = request.remote_addr  # Client's IP address
    user_agent = request.headers.get('User-Agent')  # User agent info
    logger.info(f"Home page accessed from {user_ip} | User-Agent: {user_agent}")

    #try:
    #    return render_template('index.html')
    #except Exception as e:
    #    logger.error(f"Error rendering home page: {str(e)}")
    #    return jsonify({'error': 'Internal Server Error'}), 500
    return render_template('index.html')

@main.route('/square_num/<int:num>', methods=['GET'])
def home_with_num(num):
    """
    Example route that squares a number passed in the URL:
    e.g., GET /square_num/5 -> returns 25 in JSON.
    """
    logger.info(f"Home page accessed with parameter num={num}")
    return jsonify({'data': num ** 2})

@main.route('/user/<int:userid>', methods=['GET'])
def get_user_by_id(userid):
    """
    Example route to fetch a user by ID, returning basic info as JSON.
    """
    logger.info(f"Getting user by ID {userid}")
    user = User.query.get_or_404(userid)
    return jsonify({'username': user.username, 'email': user.email})

@main.route('/register', methods=['GET', 'POST'])
def register():
    """
    User Registration Route
    - Creates a User, UserProfile, and UserMembership
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        # Check if a user with the same username or email already exists
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()
        if existing_user:
            flash("User with this username or email already exists", "error")
            return redirect(url_for('main.register'))
        
        # Create User (authentication info)
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )

        # Create UserProfile (personal info)
        new_user_profile = UserProfile(
            user=new_user,
        )

        # Create UserMembership (membership info)
        new_user_membership = UserMembership(
            user_profile=new_user_profile,
            membership_type="customer",
            submembership_type="basic",
            created_at=datetime.utcnow()
        )

        try:
            # Commit all to the database
            db.session.add(new_user)
            db.session.add(new_user_profile)
            db.session.add(new_user_membership)
            db.session.commit()

            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('main.login'))
        except IntegrityError:
            db.session.rollback()
            flash("There was an issue registering your account.", "danger")
            return redirect(url_for('main.register'))

    # GET request or invalid form
    return render_template('register.html', form=form)

def profile_has_changed(form, profile):
    # Compare each field – adjust field names as necessary.
    return (
        form.username.data != profile.username or
        form.email.data != profile.email or
        form.first_name.data != profile.first_name or
        form.last_name.data != profile.last_name or
        form.phone_country_code.data != profile.phone_country_code or
        form.phone_area_code.data != profile.phone_area_code or
        form.phone_number.data != profile.phone_number or
        form.street_address.data != profile.street_address or
        form.city.data != profile.city or
        form.state.data != profile.state or
        form.zip_code.data != profile.zip_code or
        form.birthdate.data != profile.birthdate or
        form.membership_type.data != profile.membership_type or
        form.submembership_type.data != profile.submembership_type
    )

@main.route('/profile', methods=['GET', 'POST'])
def profile():
    """
    User Profile Route
    - Fetches the UserProfile based on the session user_id
    - Displays personal info, membership info, and PDF of the profile
    """
    error = None

    # Ensure the user is logged in
    if 'user_id' not in session:
        error="Please log in to view your profile."
        flash("Please log in to view your profile.", "warning")
        return redirect(url_for('main.login'))  # Adjust to your actual login endpoint

        # Fetch the UserProfile based on the session user_id
    try:
        # Get the user_id from the session if available, else get from the URL parameter
        user_id = request.args.get('user_id') or session.get('user_id')
    except KeyError:
        error="Invalid user ID."
        flash("User need to login first", "error")
        return redirect(url_for('main.login'))
    
    user_profile = UserProfile.query.get_or_404(user_id)
    # Assuming the UserProfile has a relationship to User (e.g., user_profile.user)
    user = user_profile.user 
    # Retrieve membership if available (adjust attribute/relationship as needed)
    user_membership = UserMembership.query.filter_by(user_profile_id=user_profile.id).first()

    # Create the form, pre-populated with the user's current profile data
    form = ProfileForm(obj=user_profile)

    # Optionally pre-populate fields from the associated User and Membership objects
    #if user_id:
        #form.username.data = user.username
        #form.email.data = user.email
        #form.first_name.data = user_profile.first_name
        #form.last_name.data = user_profile.last_name
        #form.phone_country_code.data = user_profile.phone_country_code
        #form.phone_area_code.data = user_profile.phone_area_code
        #form.phone_number.data = user_profile.phone_number
        #form.street_address.data = user_profile.street_address
        #form.city.data = user_profile.city
        #form.state.data = user_profile.state
        #form.zip_code.data = user_profile.zip_code
        #form.birthdate.data = user_profile.birthdate
        #form.membership_type.data = user_membership.membership_type
        #form.submembership_type.data = user_membership.submembership_type

    if form.validate_on_submit():
        # Create a helper function to compare the form with the current profile.
        if not profile_has_changed(form, user_profile):
            flash('No changes made.', 'info')
            return redirect(url_for('/'))
        
        # Update User data
        user.username = form.username.data
        user.email = form.email.data

        # Optionally update password if the form contains a password field and it's non-empty
        if form.password.data:
            user.password = generate_password_hash(form.password.data)

        db.session.add(user)

        # Update UserProfile (personal info)
        user_profile.first_name = form.first_name.data
        user_profile.last_name = form.last_name.data
        user_profile.phone_country_code = form.phone_country_code.data
        user_profile.phone_area_code = form.phone_area_code.data
        user_profile.phone_number = form.phone_number.data
        user_profile.street_address = form.street_address.data
        user_profile.city = form.city.data
        user_profile.state = form.state.data
        user_profile.zip_code = form.zip_code.data
        user_profile.birthdate = form.birthdate.data

        db.session.add(user_profile)

        # Update or create UserMembership (membership info)
        user_membership.membership_type = form.membership_type.data
        user_membership.submembership_type = form.submembership_type.data

        db.session.add(user_membership)

        db.session.commit()
        # Redirect to profile page after successful update
        flash("Your profile has been updated successfully!", "success")
        return redirect(url_for('main.profile'))

    return render_template('profile.html', form=form, config=DevelopmentConfig, user_profile=user_profile, user=user, user_membership=user_membership, error=error)

@main.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route that checks both a mock_users dict (for demo)
    and the real database for valid credentials.
    """
    error = None
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data

        # 1) Check mock_users (demo only)
        #if username in mock_users:
        #    mock_user_data = mock_users[username]
        #    if password == mock_user_data["password"]:
        #        session['user_id'] = username  # storing email as an ID for the mock user
        #        #session['is_vendor'] = mock_user_data['is_vendor']
        #        logger.info(
        #            f"Mock user logged in: {username} "
        #            f"({'Vendor' if mock_user_data['is_vendor'] else 'Customer'})"
        #        )
        #        return redirect(url_for('main.profile'))

        # Find the user by username
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id  # In a real app, consider more robust session management.
            session['username'] = user.username
            session['user_profile_id'] = user.profile.id if user.profile else None
            session['user_profile'] = user.profile.to_dict() if user.profile else {}
            session['user_membership_id'] = user.profile.membership.id if user.profile.membership else None
            session['user_membership'] = user.profile.membership.to_dict() if user.profile.membership else {}

            # In a real app, consider storing user profile data in a session or a database.
            # session['user_profile_pdf'] = generate_pdf(user.profile) if user.profile else None
            # session['user_profile_pdf_filename'] = generate_pdf_filename(user.profile) if user.profile else None
            # session['user_profile_pdf_timestamp'] = user.profile.pdf_timestamp if user.profile else None
            # session['user_profile_pdf_url'] = url_for('static', filename=session['user_profile_pdf_filename']) if session['user_profile_pdf_filename'] else None
            # session['user_profile_pdf_last_updated'] = user.profile.pdf_timestamp.strftime('%Y-%m-%d %H:%M:%S') if user.profile else None
            # session['user_profile_pdf_last_updated_formatted'] = user.profile.pdf_timestamp.strftime('%Y-%m-%d %H:%M:%S') if user.profile else None


            # Determine membership status via the user's membership if available.
            #membership = user.profile.membership if user.profile else None
            #is_vendor = (membership.membership_type == 'vendor') if membership else False
            #session['is_vendor'] = is_vendor

            # logger.info(
            #     f"User logged in: {user.username} "
            #     f"({'Vendor' if is_vendor else 'Customer'})"
            # )
            # return redirect(url_for('main.dashboard'))

            logger.info(f"User logged in: {user.username} ")
            flash('Login successful.', 'success')
            return redirect(url_for('main.profile'))
        else:
        # If no valid credentials found, flash an error and reload the login page.
            logger.warning(f"Failed login attempt for username: {username}")
            error = 'Login failed'
            flash("Invalid credentials. Please try again.", "danger")
            return redirect(url_for('main.login'))

    # On GET (or if form didn't validate), render the login page with the form.
    return render_template('login.html', form=form, error=error)

@main.route('/logout')
def logout():
    """
    Log out the user by clearing session data.
    """
    session.pop('user_id', None)
    session.pop('is_vendor', None)
    return redirect(url_for('main.login'))

@main.route('/contact')
def contact():
    """
    Contact page route
    """
    logger.info("Contact page accessed")
    return render_template('contact.html')

@main.route('/about_us')
def about_us():
    """
    About Us page route
    """
    logger.info("About Us page accessed")
    return render_template('about_us.html')

@main.route('/pdf_report', methods=['POST'])
def generate_pdf_report():
    """
    Generates a PDF membership report for the logged-in user
    using ReportLab and returns it as a downloadable file.
    """
    if 'user_id' not in session:
        logger.warning("Unauthorized access attempt to generate PDF report.")
        return redirect(url_for('main.login'))

    # If the user_id is from mock_users, skip real DB
    if isinstance(session['user_id'], str) and session['user_id'] in mock_users:
        user_email = session['user_id']
        user_type = "Vendor" if mock_users[user_email]['is_vendor'] else "Customer"
        membership_type = "vendor" if mock_users[user_email]['is_vendor'] else "customer"
        submembership_type = "N/A (mock user)"
        username = user_email
    else:
        # Otherwise, fetch from DB
        user_id = session['user_id']
        user = User.query.get(user_id)
        if not user or not user.profile or not user.profile.membership:
            logger.error(f"No valid membership found for user_id={user_id}")
            flash("No valid membership found.", "danger")
            return redirect(url_for('main.dashboard'))

        username = user.username
        membership_type = user.profile.membership.membership_type
        submembership_type = user.profile.membership.submembership_type
        user_type = "Vendor" if membership_type == 'vendor' else "Customer"

    logger.info(
        f"Generating PDF report for user: {username} "
        f"({user_type} / membership_type={membership_type})"
    )

    # Build PDF
    doc = SimpleDocTemplate("membership_report.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Membership Report", styles['h1']))
    story.append(Paragraph(f"User: {username}", styles['h2']))
    story.append(Paragraph(f"Membership Type: {membership_type}", styles['h3']))
    story.append(Paragraph(f"Subscription Level: {submembership_type}", styles['h3']))

    doc.build(story)

    return send_file("membership_report.pdf", as_attachment=True)

@main.route('/dashboard')
def dashboard():
    """
    Dashboard route that shows different views based on whether the user is a vendor or customer.
    """
    if 'user_id' not in session:
        logger.warning("Unauthorized access attempt to dashboard.")
        return redirect(url_for('main.login'))

    if session.get('is_vendor'):
        logger.debug(f"Vendor dashboard accessed by user_id={session['user_id']}")
        return render_template('vendor_dashboard.html')
    else:
        logger.debug(f"Customer dashboard accessed by user_id={session['user_id']}")
        return render_template('customer_dashboard.html')

@main.route('/admin-dashboard')
def adminDashboard():
    """
    Dashboard route that shows different views based on whether the user is a vendor or customer.
    """
    if 'user_id' not in session:
        logger.warning("Unauthorized access attempt to dashboard.")
        return redirect(url_for('main.login'))

    if session.get('is_admin'):
        logger.debug(f"Admin dashboard accessed by user_id={session['user_id']}")
        return render_template('admin_dashboard.html')
    else:
        logger.debug(f"Attempted Admin dashboard accessed by user_id={session['user_id']}")
        return redirect(url_for('/'))


# Attach a Flask-RESTful API to this blueprint
api = Api(main)

# Register the Resources with their endpoints
api.add_resource(Hello, '/api')
api.add_resource(Square, '/api/square/<int:num>')
api.add_resource(apiLogin, '/api/login')
api.add_resource(apiRegister, '/api/register')
api.add_resource(getSubmembershipTypes, '/api/submembership_types/<string:membership_type>')
