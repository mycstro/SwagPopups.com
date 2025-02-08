import datetime
import jwt

from flask import request, jsonify, current_app
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Import your database and models
from .models import db, User

# Example data structure for submembership types
# (You might have this in a config or separate file)
SUBMEMBERSHIP_TYPES = {
    'customer': ['basic', 'premium', 'vip'],
    'vendor': ['starter', 'enterprise', 'pro'],
    'supplier': ['local', 'regional', 'global'],
    'distributor': ['regional', 'national', 'international'],
    'reseller': ['silver', 'gold', 'platinum'],
    'affiliate': ['bronze', 'silver', 'gold'],
    'partner': ['strategic', 'operational'],
    'franchisee': ['entry', 'growth', 'executive']
}

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'hello world'})

    def post(self):
        data = request.get_json()
        return jsonify({'data': data}), 201


class Square(Resource):
    def get(self, num):
        return jsonify({'square': num ** 2})


class apiLogin(Resource):
    def get(self):
        return jsonify({'message': 'API endpoint for login'})

    def post(self):
        """
        Checks for JSON payload first.
        If not JSON, fallback to query parameters (?email=...&password=...).
        """
        if request.is_json:
            data = request.get_json()  # Get JSON data
            email = data.get('email')
            password = data.get('password')
        else:
            # If not JSON, fetch from URL parameters
            email = request.args.get('email')
            password = request.args.get('password')

        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'message': 'User not found'}), 404

        if check_password_hash(user.password, password):
            # Create a JWT token
            token = jwt.encode(
                {
                    'user_id': user.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
                },
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            return jsonify({
                'token': token,
                'username': user.username,
                # If you’re storing membership_type in UserProfile/UserMembership,
                # you would retrieve it from there instead. Example:
                # 'membership_type': user.profile.membership.membership_type if user.profile and user.profile.membership else None
                'membership_type': user.membership_type  
            })
        else:
            return jsonify({'message': 'Wrong password'}), 401


class getSubmembershipTypes(Resource):
    def get(self, membership_type):
        return jsonify(SUBMEMBERSHIP_TYPES.get(membership_type, []))


class apiRegister(Resource):
    def post(self):
        data = request.get_json()
        required_fields = [
            'username', 'email', 'password', 'first_name', 'last_name',
            'phone_country_code', 'phone_area_code', 'phone_number',
            'street_address', 'city', 'state', 'zip_code', 'birthdate',
            'membership_type', 'submembership_type'
        ]

        # Ensure all required fields are present
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        # Check if user with this username or email already exists
        existing_user = User.query.filter(
            (User.username == data['username']) | (User.email == data['email'])
        ).first()
        if existing_user:
            return jsonify({'error': 'User with this username or email already exists'}), 400

        try:
            hashed_pw = generate_password_hash(data['password'])
            # Create the user directly in User model
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=hashed_pw,
                first_name=data['first_name'],
                last_name=data['last_name'],
                phone_country_code=data['phone_country_code'],
                phone_area_code=data['phone_area_code'],
                phone_number=data['phone_number'],
                street_address=data['street_address'],
                city=data['city'],
                state=data['state'],
                zip_code=data['zip_code'],
                birthdate=data['birthdate'],
                membership_type=data['membership_type'],
                submembership_type=data['submembership_type']
            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'message': 'User registered successfully'}), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Database error. Please try again'}), 500
