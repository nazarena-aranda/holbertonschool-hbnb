import re
from app.models.base_model import BaseModel
from app import bcrypt, db

class User(BaseModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, first_name, last_name, email, is_admin=False, password=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        if password:
            self.hash_password(password)

    def validate(self):
        errors = []
        if not self.first_name:
            errors.append("First name is required")
        if not self.last_name:
            errors.append("Last name is required")
        if not self.password:
            errors.append("Password is required")
        if not self.email:
            errors.append("Email is required")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            errors.append("Invalid email format")
        return errors
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)
