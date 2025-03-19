import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app import db

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utc)
    updated_at = Column(DateTime, default=datetime.utc, onupdate=datetime.utc)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()