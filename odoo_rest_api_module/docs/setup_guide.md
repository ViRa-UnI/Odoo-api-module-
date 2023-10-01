# Odoo REST API Module Setup Guide

This guide will walk you through the process of setting up the Odoo REST API module.

## Prerequisites

- Odoo instance up and running.
- Python 3.6 or higher installed.
- Redis server installed for rate limiting feature.
- Access to the command line on the server where Odoo is installed.

## Installation

1. Download or clone the `odoo_rest_api_module` repository to your local machine.

2. Copy the `odoo_rest_api_module` folder into the Odoo addons directory. The exact location may vary depending on your Odoo installation.

3. Restart your Odoo server.

4. Navigate to the Apps menu in the Odoo web interface, remove the 'Apps' filter and search for `odoo_rest_api_module`.

5. Click on `Install` to install the module.

## Configuration

1. Navigate to the `Settings` menu in the Odoo web interface.

2. Search for `odoo_rest_api_module` and click on it.

3. Here you can configure the settings for the module such as rate limiting rules, JWT secret key, and more.

## Usage

1. To use the API, you first need to authenticate. Send a POST request to the `/auth/login` endpoint with your Odoo username and password in the body.

2. If the credentials are correct, the server will respond with a JWT token. This token must be included in the `Authorization` header of all subsequent requests.

3. To access data, send a GET request to the desired endpoint. For example, to get a list of all users, send a GET request to `/api/users`.

4. To create, update, or delete data, send a POST, PUT, or DELETE request to the appropriate endpoint with the data in the body.

## Testing

1. Automated tests are located in the `odoo_rest_api_module/tests` directory.

2. To run the tests, navigate to the Odoo root directory and run the following command: `python3 -m unittest discover odoo_rest_api_module/tests`.

## Documentation

- Detailed API documentation can be found in the `odoo_rest_api_module/docs/api_documentation.md` file.

- Sample requests and responses for each endpoint can be found in the `odoo_rest_api_module/docs/sample_requests_responses.md` file.

## Support

If you encounter any issues or have any questions, please open an issue on the `odoo_rest_api_module` GitHub repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.