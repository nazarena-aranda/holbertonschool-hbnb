from app.models.base_model import BaseModel
from app import bcrypt, db


class Amenity(BaseModel):
    __tablename__ = 'amenities'

    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        super().__init__()
        self.name = name

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            if name == "":
                raise ValueError("Name must not be empty")
            self._name = name