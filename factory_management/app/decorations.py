from functools import wraps
from flask import request, jsonify
from app.utils.util import decode_token
from app.models import User

def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            payload = decode_token(token)
            if isinstance(payload, str):  # Error message
                return jsonify({'message': payload}), 401

            user_id = payload['sub']
            user = User.query.get(user_id)
            if not user:
                return jsonify({'message': 'User not found'}), 404

            if user.role != role:
                return jsonify({'message': 'Access forbidden: insufficient rights'}), 403

            return fn(*args, **kwargs)
        return decorated_function
    return wrapper
