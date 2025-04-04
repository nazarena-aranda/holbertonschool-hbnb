from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade
from flask_jwt_extended import jwt_required
from app.models.user import User

api = Namespace('auth', description='Authentication operations')

login_model = api.model('Login', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password')
})

signup_model = api.model('Signup', {
    'email': fields.String(required=True, description='User email'),
    'password': fields.String(required=True, description='User password'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name')
})

@api.route('/signup')
class Signup(Resource):
    @api.expect(signup_model)
    def post(self):
        """Register a new user"""
        user_data = api.payload
       
        try:
            created_user = facade.create_user({
                "first_name": user_data.get('first_name'),
                "last_name": user_data.get('last_name'),
                "email": user_data.get('email'),
                "password": user_data.get('password'),
                "is_admin": False,
            })

            access_token = create_access_token(identity=str(created_user.id), additional_claims={'is_admin': created_user.is_admin})
            return {'message': 'User created successfully', 'access_token': access_token}, 201
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': str(e)}, 500

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Authenticate user and return a JWT token"""
        credentials = api.payload
        user = facade.get_user_by_email(credentials['email'])
        
        if not user or not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401
            
        if not user.verify_password(credentials['password']):
            return {'error': 'Invalid credentials'}, 401
            
        access_token = create_access_token(identity=str(user.id), additional_claims={'is_admin': user.is_admin})
        return {'access_token': access_token}, 200
