import re
from app.models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

    def validate(self):
        errors = []
        if not self.first_name:
            errors.append("First name is required")
        if not self.last_name:
            errors.append("Last name is required")
        if not self.email:
            errors.append("Email is required")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            errors.append("Invalid email format")
        return errors