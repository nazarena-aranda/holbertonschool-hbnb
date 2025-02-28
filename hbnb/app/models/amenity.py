from app.models.base_model import BaseModel

class Amenity(BaseModel):
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