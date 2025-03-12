from flask_restx import Namespace, Resource, fields
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
    def post(self):
        """Create a new user with validation"""
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
            created_user = facade.create_user(user)
            return api.marshal(created_user, user_model), 201
        except Exception as e:
            return {'error': str(e)}, 500