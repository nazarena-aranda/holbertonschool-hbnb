from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.models.user import User
from app.services import facade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email address'),
    'password': fields.String(required=True, description='Password'),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    @api.response(201, 'User created successfully')
    @api.response(400, 'Invalid input')
    @api.response(409, 'Email already exists')
    @jwt_required()
    def post(self):
        """Create a new user with validation"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload

        user = User(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            email=user_data.get('email'),
            password=user_data.get('password')
        )

        if errors := user.validate():
            return {'error': ', '.join(errors)}, 400

        if facade.get_user_by_email(user.email):
            return {'error': 'Email already registered'}, 409

        try:
            created_user = facade.create_user({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "is_admin": user.is_admin,
                "password": user.password
            })

            return api.marshal(created_user, user_model), 201
        except Exception as e:
            return {'error': str(e)}, 500

@api.route('/<user_id>')
class UserResource(Resource):
    @api.expect(user_model)
    @api.response(200, 'User updated successfully')
    @api.response(400, 'Invalid input')
    @api.response(403, 'Admin privileges required')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        """Update a user's details"""
        current_user = get_jwt_identity()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        if 'email' in user_data:
            existing_user = facade.get_user_by_email(user_data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already registered'}, 409

        try:
            updated_user = facade.update_user(user_id, user_data)
            return api.marshal(updated_user, user_model), 200
        except Exception as e:
            return {'error': str(e)}, 500