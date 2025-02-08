from datetime import datetime
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # One-to-one relationship with UserProfile.
    # Note: Use the same name for back_populates on both sides.
    profile = db.relationship('UserProfile', back_populates='user', uselist=False)

    # Removed the direct relationship to UserMembership to avoid ambiguity.
    # To access membership info, use: user.profile.membership

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(200), nullable=True)  # URL or path to image
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    phone_country_code = db.Column(db.String(5), nullable=True)
    phone_area_code = db.Column(db.String(5), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)
    street_address = db.Column(db.String(200), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)

    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Relationship to User.
    # Note: back_populates name must match the one defined on the User model.
    user = db.relationship('User', back_populates='profile')

    # One-to-one relationship with UserMembership
    membership = db.relationship('UserMembership', back_populates='user_profile', uselist=False)

    def to_dict(self):
        # This example uses a comprehension to automatically add all columns.
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class UserMembership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    membership_type = db.Column(db.String(20), nullable=False)
    submembership_type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Foreign key to UserProfile
    user_profile_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)
    
    # Relationship to UserProfile.
    # Note: back_populates here matches the attribute name on UserProfile.
    user_profile = db.relationship('UserProfile', back_populates='membership')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class AreaCodesList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_country_code = db.Column(db.String(5), unique=True, nullable=False)
    phone_area_codes = db.Column(db.Text, nullable=False)
    
    def __init__(self, phone_country_code, phone_area_codes):
        self.phone_country_code = phone_country_code
        self.phone_area_codes = phone_area_codes

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    @classmethod
    def get_area_codes(cls, phone_country_code):
        return cls.query.filter_by(phone_country_code=phone_country_code).first()
    
    @classmethod
    def get_all_area_codes(cls):
        return cls.query.all()
    
    @classmethod
    def add_area_codes(cls, phone_country_code, phone_area_codes):
        new_area_codes = cls(phone_country_code, phone_area_codes)
        db.session.add(new_area_codes)
        db.session.commit()
        return new_area_codes.to_dict()
    
    @classmethod
    def update_area_codes(cls, id, phone_area_codes):
        area_codes = cls.query.get(id)
        if area_codes:
            area_codes.phone_area_codes = phone_area_codes
            db.session.commit()
            return area_codes.to_dict()
        else:
            return None
        
    @classmethod
    def delete_area_codes(cls, id):
        area_codes = cls.query.get(id)
        if area_codes:
            db.session.delete(area_codes)
            db.session.commit()
            return True
        else:
            return False
        
    @staticmethod
    def test():
        # Test the AreaCodesList class
        db.create_all()
        AreaCodesList.test()
        db.session.remove()
        db.drop_all()

        # Create a new AreaCodesList instance
        area_codes_list = AreaCodesList('1', '["123", "456", "789"]')
        db.session.add(area_codes_list)
        db.session.commit()
        
        # Get area codes for a specific country
        area_codes = AreaCodesList.get_area_codes('1')
        print(area_codes.phone_area_codes)
        
        # Get all area codes for all countries
        all_area_codes = AreaCodesList.get_all_area_codes()
        for area_code in all_area_codes:
            print(area_code.phone_country_code, area_code.phone_area_codes)
        
        # Test the AreaCodesList class with error handling
        try:
            AreaCodesList.test()
        except Exception as e:
            print(f"Error occurred during testing: {e}")
            print("Test failed.")
            exit()
        
        # Test the AreaCodesList class with successful deletion
        deleted_status = AreaCodesList.delete_area_codes(1)
        print(f"Deleted status: {deleted_status}")
        
        print("Test passed.")
            
        # Example usage:
        # Add area codes for a specific country
        # area_codes_list = AreaCodesList.add_area_codes('1', '["123", "456", "789"]')
        # print(area_codes_list)
        
        # Update area codes for a specific country
        # updated_area_codes_list = AreaCodesList.update_area_codes(1, '["987", "654", "321"]')
        # print(updated_area_codes_list)
        
        # Delete area codes for a specific country
        # deleted_status = AreaCodesList.delete_area_codes(1)
        # print(deleted_status)
        
        # Get all area codes for a specific country
        # area_codes = AreaCodesList.get_area_codes('1')
        # print(area_codes.phone_area_codes)
        
        # Get all area codes for all countries
        # all_area_codes = AreaCodesList.get_all_area_codes()
        # for area_code in all_area_codes:
        #     print(area_code.phone_country_code, area_code.phone_area_codes)

