from app.models.base_model import BaseModel
from app import bcrypt, db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Review(BaseModel):
    __tablename__ = 'reviews'

    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.String(36), ForeignKey('users.id'), nullable=False)

    place_id = db.Column(db.String(36), ForeignKey('places.id'), nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id

    def validate(self):
        errors = []
        if not self.text:
            errors.append("Text is required")
        if not self.rating or not (1 <= self.rating <= 5):
            errors.append("Rating must be between 1 and 5")
        if not self.place_id:
            errors.append("Place ID is required")
        if not self.user_id:
            errors.append("User ID is required")
        return errors