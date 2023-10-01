```python
from odoo import http
from .main_controller import MainController
from ..models.webhook import Webhook
from ..services.logging_service import LoggingService

class WebhookController(MainController):

    @http.route('/api/webhooks', type='json', auth='user', methods=['POST'])
    def register_webhook(self, **kwargs):
        try:
            # Validate and sanitize data
            self.validate_data(kwargs, ['callback_url'])
            callback_url = kwargs.get('callback_url')

            # Create a new webhook
            webhook = Webhook.create({'callback_url': callback_url})

            # Log the request
            LoggingService.log_request(http.request.httprequest, http.request.session.uid, payload=kwargs)

            return {
                'status': 'success',
                'data': {
                    'webhook_id': webhook.id
                }
            }
        except Exception as e:
            # Log the error
            LoggingService.log_error(http.request.httprequest, http.request.session.uid, str(e))

            return {
                'status': 'error',
                'message': str(e)
            }

    @http.route('/api/webhooks/<int:webhook_id>', type='json', auth='user', methods=['DELETE'])
    def delete_webhook(self, webhook_id):
        try:
            # Find the webhook
            webhook = Webhook.search([('id', '=', webhook_id)])

            # Delete the webhook
            webhook.unlink()

            # Log the request
            LoggingService.log_request(http.request.httprequest, http.request.session.uid, payload={'webhook_id': webhook_id})

            return {
                'status': 'success',
                'message': 'Webhook deleted successfully'
            }
        except Exception as e:
            # Log the error
            LoggingService.log_error(http.request.httprequest, http.request.session.uid, str(e))

            return {
                'status': 'error',
                'message': str(e)
            }
```
