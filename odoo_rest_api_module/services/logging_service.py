```python
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class LoggingService(models.Model):
    _name = 'logging.service'

    source_ip = fields.Char(string='Source IP')
    timestamp = fields.Datetime(string='Timestamp')
    endpoint_accessed = fields.Char(string='Endpoint Accessed')
    payload = fields.Text(string='Payload')
    error = fields.Text(string='Error')

    @api.model
    def create_log(self, source_ip, endpoint_accessed, payload, error=None):
        timestamp = fields.Datetime.now()
        log = self.create({
            'source_ip': source_ip,
            'timestamp': timestamp,
            'endpoint_accessed': endpoint_accessed,
            'payload': payload,
            'error': error
        })
        _logger.info(f'Log created: {log.id}')
        return log

    @api.model
    def secure_store(self, log):
        # Implement encryption for sensitive data here
        pass
```