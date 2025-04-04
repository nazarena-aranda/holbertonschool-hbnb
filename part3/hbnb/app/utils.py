from flask_jwt_extended import get_jwt_identity, get_jwt

def get_current_user():
    identity = get_jwt_identity()
    claims = get_jwt()
    return {
        'id': identity,
        'is_admin': claims.get('is_admin')
}