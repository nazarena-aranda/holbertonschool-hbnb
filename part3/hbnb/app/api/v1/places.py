from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from app.services import facade
from app.utils import get_current_user

api = Namespace('places', description='Place operations')

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new place"""
        current_user = get_current_user()
        place_data = api.payload
        place_data['owner_id'] = current_user.get('id')

        try:
            new_place = facade.create_place(place_data)
            return {
                'id': new_place.id,
                'title': new_place.title,
                'description': new_place.description,
                'price': new_place.price,
                'latitude': new_place.latitude,
                'longitude': new_place.longitude,
                'owner': {
                    'id': new_place.owner.id,
                    'first_name': new_place.owner.first_name,
                    'last_name': new_place.owner.last_name,
                    'email': new_place.owner.email,
                },
                'amenities': [
                    {
                        'id': amenity.id,
                        'name': amenity.name,
                    } 
                    for amenity in new_place.amenities
                ],
                'reviews': [
                    {
                        'id': review.id,
                        'text': review.text,
                        'rating': review.rating,
                    }
                    for review in new_place.reviews
                ],
            }, 201
        except ValueError as e:
            return {'error': str(e)}, 400

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()
        return [{
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude
        } for place in places], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name,
                'email': place.owner.email
            },
            'amenities': [
                {
                    'id': amenity.id, 
                    'name': amenity.name
                } 
                for amenity in place.amenities
            ],
            'reviews': [
                {
                    'id': review.id,
                    'text': review.text,
                    'rating': review.rating,
                    'author': {
                        'id': review.author.id,
                        'first_name': review.author.first_name,
                        'last_name': review.author.last_name
                    }
                }
                for review in place.reviews
            ]
        }, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        current_user = get_current_user()
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        place_data = api.payload
        try:
            updated_place = facade.update_place(place_id, place_data)
            return {'message': 'Place updated successfully'}, 200
        except ValueError as e:
            return {'error': str(e)}, 400