# Odoo REST API Module - API Documentation

This document provides a comprehensive guide to the endpoints provided by the Odoo REST API Module.

## Authentication

### POST /api/auth/token

Generate a new JWT token.

**Request Body:**

```json
{
  "username": "string",
  "password": "string"
}
```

**Response:**

```json
{
  "token": "string"
}
```

### POST /api/auth/refresh

Refresh an existing JWT token.

**Request Headers:**

```json
{
  "Authorization": "Bearer {token}"
}
```

**Response:**

```json
{
  "token": "string"
}
```

## Logging

Logs are automatically captured for each request and include details such as source IP, timestamp, endpoint accessed, payload, and any errors.

## Rate Limiting

Rate limiting is implemented using Redis. The limits are customizable based on user roles or API keys.

## Pagination & Filtering

Endpoints that return a list of resources support pagination and filtering. Use the `page` query parameter to specify the page number and `limit` to specify the number of items per page. Use the `sort` query parameter to sort the results.

## Dynamic Data Access

The API supports GraphQL for dynamic data access. Use the `/api/graphql` endpoint to make GraphQL queries.

## API Versioning

The API version is included in the URL, e.g., `/api/v1/`.

## Webhooks

### POST /api/webhooks

Register a new webhook.

**Request Body:**

```json
{
  "url": "string",
  "events": ["string"]
}
```

**Response:**

```json
{
  "id": "string",
  "url": "string",
  "events": ["string"]
}
```

## Data Validation & Sanitization

All incoming data is validated and sanitized to prevent SQL injections or similar attacks.

For more detailed information about each endpoint, including possible error codes and their meanings, please refer to the auto-generated Swagger documentation.