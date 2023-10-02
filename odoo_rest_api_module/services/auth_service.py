```python
from odoo import api, models
import jwt
import datetime

class AuthService(models.Model):
    _name = 'auth.service'

    @api.model
    def generate_token(self, user_id, user_role):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id,
                'role': user_role
            }
            return jwt.encode(
                payload,
                'SECRET_KEY',  # This should be replaced with a secret key stored securely
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @api.model
    def decode_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, 'SECRET_KEY')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @api.model
    def validate_token(self, auth_token):
        user_id = self.decode_token(auth_token)
        if not isinstance(user_id, str):
            return True
        else:
            return False

    @api.model
    def refresh_token(self, auth_token):
        user_id = self.decode_token(auth_token)
        user_role = self.env['res.users'].browse(user_id).role
        if not isinstance(user_id, str):
            return self.generate_token(user_id, user_role)
        else:
            return 'Invalid token. Please log in again.'
```
