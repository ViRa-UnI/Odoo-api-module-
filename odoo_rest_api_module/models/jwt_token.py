```python
from odoo import models, fields, api
import jwt
import datetime

class JWTToken(models.Model):
    _name = 'jwt.token'
    _description = 'JWT Token Model'

    token = fields.Char(string='Token', required=True, readonly=True)
    user_id = fields.Many2one('res.users', string='User', required=True, readonly=True)
    expiration_date = fields.Datetime(string='Expiration Date', required=True, readonly=True)

    @api.model
    def create_token(self, user_id):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            'YOUR_SECRET_KEY', 
            algorithm='HS256'
        )

    @api.model
    def validate_token(self, token):
        try:
            payload = jwt.decode(token, 'YOUR_SECRET_KEY')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Token expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    @api.model
    def refresh_token(self, token):
        try:
            payload = jwt.decode(token, 'YOUR_SECRET_KEY')
            new_token = self.create_token(payload['sub'])
            return new_token
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
```
