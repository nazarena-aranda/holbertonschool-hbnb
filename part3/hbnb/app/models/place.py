from app.models.base_model import BaseModel
from app import bcrypt, db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String(36), db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    user_id = db.Column(db.String(36), ForeignKey('users.id'), nullable=False)
    owner = relationship("User", backref="places")

    reviews = relationship("Review", backref="place", lazy=True)

    amenities = relationship("Amenity", secondary=place_amenity, backref="places", lazy=True)

    def __init__(self, title, description, price, latitude, longitude, owner, reviews=[], amenities=[]):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = reviews
        self.amenities = amenities

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, name):
        if name == "":
            raise ValueError("Title must not be empty")
        self._title = name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description ):
        if description == "":
            raise ValueError("Description must not be empty")
        self._description = description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be a non negative float")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

    def validate(self):
        if not self.title:
            errors.append("Title is required")
        if self.price <= 0:
            errors.append("Price must be positive")
        if not (-90 <= self.latitude <= 90):
            errors.append("Latitude must be between -90 and 90")
        if not (-180 <= self.longitude <= 180):
            errors.append("Longitude must be between -180 and 180")
        return errors