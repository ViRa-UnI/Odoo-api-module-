```python
from odoo import http
from odoo.http import request
from .main_controller import MainController
from ..services.auth_service import AuthService
from ..services.logging_service import LoggingService

class AuthController(MainController):

    @http.route('/api/auth/token', type='http', auth='none', methods=['POST'], csrf=False)
    def generate_token(self, **kwargs):
        try:
            username = kwargs.get('username')
            password = kwargs.get('password')
            if not username or not password:
                return self.error_response('Missing username or password', 400)

            auth_service = AuthService()
            token = auth_service.generate_token(username, password)
            if not token:
                return self.error_response('Invalid username or password', 401)

            return self.success_response({'token': token})

        except Exception as e:
            LoggingService.log_exception(e)
            return self.error_response('Internal server error', 500)

    @http.route('/api/auth/refresh', type='http', auth='none', methods=['POST'], csrf=False)
    def refresh_token(self, **kwargs):
        try:
            refresh_token = kwargs.get('refresh_token')
            if not refresh_token:
                return self.error_response('Missing refresh token', 400)

            auth_service = AuthService()
            new_token = auth_service.refresh_token(refresh_token)
            if not new_token:
                return self.error_response('Invalid refresh token', 401)

            return self.success_response({'token': new_token})

        except Exception as e:
            LoggingService.log_exception(e)
            return self.error_response('Internal server error', 500)
```