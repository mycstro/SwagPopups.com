from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    SubmitField,
    DateField
)
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    Regexp,
    Optional
)
from api.config import DevelopmentConfig

# ------------------------
# 3. Define the available country codes
#    (You can add as many as you like or pull from an external source)
# ------------------------
COUNTRY_CODES = DevelopmentConfig.COUNTRYCODES
#AREA_CODES = DevelopmentConfig.AREACODES
# Use a list comprehension to create (value, label) tuples if needed.
#AREA_CODES = [(code, code) for code in DevelopmentConfig.AREACODES]
#AREA_CODES = [(location, codes) for location, codes in DevelopmentConfig.AREACODES.items()]
# Convert the dictionary to a list of tuples for optgroup support.
# Each tuple is (group_label, list_of_(value, label)_tuples)
#AREA_CODES = [(group, codes) for group, codes in DevelopmentConfig.AREACODES.items()]

US_STATES = DevelopmentConfig.USSTATES

MEMBERSHIP_TYPES = [
    ('customer', 'Customer'),
    ('vendor', 'Vendor'),
    ('supplier', 'Supplier'),
    ('distributor', 'Distributor'),
    ('reseller', 'Reseller'),
    ('affiliate', 'Affiliate'),
    ('partner', 'Partner'),
    ('franchisee', 'Franchisee')
]

class LoginForm(FlaskForm):
    """
    Login form that collects user data for logging in as User 1
    """
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=4, max=80, message='Username must be between 4 and 80 characters.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Password must be at least 6 characters long.')
        ]
    )

    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    """
    Registration form that collects user data across:
    - User (username, email, password)
    - UserProfile (first_name, last_name, phone, address, birthdate)
    - UserMembership (membership_type, submembership_type)
    """

    # ----------------- USER FIELDS ----------------- #
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=4, max=80, message='Username must be between 4 and 80 characters.')
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message='Invalid email address.')
            # If you have WTForms Email with check_deliverability, you could use:
            # Email(check_deliverability=True, message='Invalid or undeliverable email address.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message='Password must be at least 6 characters long.')
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    # ----------------- SUBMIT BUTTON ----------------- #
    submit = SubmitField('Register')

class ProfileForm(FlaskForm):
    """
    Profile form that collects user profile data across:
    - UserProfile (first_name, last_name, phone, address, birthdate)
    """

    # ---------------- User --------------------------------#
    username = StringField(
        'Username',
        validators=[
            Optional(),
            Length(min=4, max=80, message='Username must be between 4 and 80 characters.')
        ]
    )
    email = StringField(
        'Email',
        validators=[
            Optional(),
            Email(message='Invalid email address.')
            # If you have WTForms Email with check_deliverability, you could use:
            # Email(check_deliverability=True, message='Invalid or undeliverable email address.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            Optional(),
            Length(min=6, message='Password must be at least 6 characters long.')
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            Optional(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
    
     # ----------------- USER PROFILE FIELDS ----------------- #
    first_name = StringField(
        'First Name',
        validators=[Optional(), Length(min=1, max=50)]
    )
    last_name = StringField(
        'Last Name',
        validators=[Optional(), Length(min=1, max=50)]
    )
    phone_country_code = SelectField(
        'Country Code',
        choices=COUNTRY_CODES,
        validators=[Optional()]
    )
    phone_area_code = SelectField(
        'Area Code',
        choices=[("", "Select a location")] + [(loc, loc) for loc in DevelopmentConfig.AREA_CODES_BY_LOCATION.keys()],        
        validators=[Optional()]
    )
    phone_number = StringField(
        'Phone Number',
        validators=[
            Optional(),
            # Updated RegExp to require 7–15 digits
            Regexp(r'^\d{7,15}$', message='Enter a valid phone number (7 to 15 digits).')
        ]
    )
    street_address = StringField(
        'Street Address',
        validators=[Optional(), Length(max=200)]
    )
    city = StringField(
        'City',
        validators=[Optional(), Length(max=100)]
    )
    state = SelectField(
        'State',
        choices=US_STATES,
        validators=[Optional(), Length(max=100)]
    )
    zip_code = StringField(
        'Zip Code',
        validators=[Optional(), Length(max=10)]
    )
    birthdate = DateField(
        'Birthdate (YYYY-MM-DD)',
        validators=[Optional()],
        format='%Y-%m-%d'
    )

    # ----------------- USER MEMBERSHIP FIELDS ----------------- #
    membership_type = SelectField(
        'Membership Type',
        choices=MEMBERSHIP_TYPES,
        validators=[Optional()]
    )
    submembership_type = SelectField(
        'Subscription Level',
        # This is empty by default. Consider dynamically populating 
        # or replacing with fixed values if you need default choices.
        choices=[],
        validators=[Optional()]
    )

    # ----------------- SUBMIT BUTTON ----------------- #
    submit = SubmitField('Update Profile')

