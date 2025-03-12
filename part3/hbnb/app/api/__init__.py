from flask_restx import Api
from flask import Blueprint
from app.api.v1.users import api as users_ns
from app.api.v1.places import api as places_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, doc='/doc/')

api.add_namespace(users_ns)
api.add_namespace(places_ns)
api.add_namespace(amenities_ns)
api.add_namespace(reviews_ns)