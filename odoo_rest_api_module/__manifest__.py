{
    'name': 'Odoo REST API Module',
    'version': '1.0',
    'category': 'API',
    'summary': 'A comprehensive Odoo REST API module',
    'sequence': 1,
    'author': 'Your Name',
    'website': 'Your Website',
    'description': """
Odoo REST API Module
====================

This module provides a standardized interface for third-party applications to interact with Odoo, emphasizing security, scalability, and extensibility.

Main Features
-------------
* Custom Authentication using JWT (JSON Web Tokens)
* Logging of request details
* Rate Limiting using Redis
* Pagination & Filtering
* Dynamic Data Access using GraphQL
* API Versioning
* Webhooks for real-time updates
* Data Validation & Sanitization
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}