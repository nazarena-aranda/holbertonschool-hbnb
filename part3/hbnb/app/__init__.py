from flask import Flask
from flask_restx import Api
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_jwt_extended import JWTManager


bcrypt = Bcrypt()
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.models.user import User
        from app.models.place import Place
        from app.models.amenity import Amenity
        from app.models.review import Review

        db.create_all()

    api = Api(app)

    from app.api.v1.auth import api as auth_ns  
    from app.api.v1.users import api as users_ns
    from app.api.v1.places import api as places_ns
    from app.api.v1.amenities import api as amenities_ns
    from app.api.v1.reviews import api as review_ns

    # Register the users namespace
    api.add_namespace(auth_ns, path='/api/v1/auth')

    api.add_namespace(users_ns, path='/api/v1/users')

    api.add_namespace(places_ns, path='/api/v1/places')

    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    api.add_namespace(review_ns, path='/api/v1/reviews')

    

    return app