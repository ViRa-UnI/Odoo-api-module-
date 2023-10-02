```python
from odoo import models, fields

class Webhook(models.Model):
    _name = 'odoo_rest_api_module.webhook'
    _description = 'Webhook Model'

    name = fields.Char(string='Name', required=True)
    url = fields.Char(string='URL', required=True)
    model_id = fields.Many2one('ir.model', string='Model', required=True)
    action = fields.Selection([
        ('create', 'On Creation'),
        ('write', 'On Update'),
        ('unlink', 'On Deletion'),
    ], string='Trigger Action', required=True)

    def trigger_webhook(self, action, record):
        if self.action == action:
            # Here you can implement the logic to send the data to the registered URL
            # You can use the `requests` library to send a POST request
            pass
```
