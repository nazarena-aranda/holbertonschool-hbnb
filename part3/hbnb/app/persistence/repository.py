from abc import ABC, abstractmethod
from app import db

class Repository:
    def add(self, obj):
        raise NotImplementedError

    def get(self, obj_id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def update(self, obj_id, data):
        raise NotImplementedError

    def delete(self, obj_id):
        raise NotImplementedError

    def get_by_attribute(self, attr_name, attr_value):
        raise NotImplementedError

class SQLAlchemyRepository(Repository):
    def __init__(self, model):
        self.model = model

    def add(self, obj):
        db.session.add(obj)
        db.session.commit()

    def get(self, obj_id):
        return self.model.query.get(obj_id)

    def get_all(self):
        return self.model.query.all()

    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)
            db.session.commit()

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            db.session.delete(obj)
            db.session.commit()

    def get_by_attribute(self, attr_name, attr_value):
        return self.model.query.filter_by(**{attr_name: attr_value}).first()

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        from app.models.user import User 
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()

class PlaceRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Place)


class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)


class AmenityRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Amenity)