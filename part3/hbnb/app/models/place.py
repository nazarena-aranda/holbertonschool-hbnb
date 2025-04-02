from app.models.base_model import BaseModel
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String(36), db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = 'places'

    # Database columns
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String(36), ForeignKey('users.id'), nullable=False)

    # Relationships
    reviews = relationship("Review", backref="place", lazy=True)
    amenities = relationship("Amenity", secondary=place_amenity, backref="places", lazy=True)

    def __init__(self, title, description, price, latitude, longitude, owner_id, reviews=None, amenities=None):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.reviews = reviews or []
        self.amenities = amenities or []

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def validate(self):
        errors = []
        if not self.title:
            errors.append("Title is required")
        if self.price <= 0:
            errors.append("Price must be positive")
        if not (-90 <= self.latitude <= 90):
            errors.append("Latitude must be between -90 and 90")
        if not (-180 <= self.longitude <= 180):
            errors.append("Longitude must be between -180 and 180")
        return errors