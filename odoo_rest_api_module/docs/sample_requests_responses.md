# Sample Requests and Responses

This document provides examples of requests and responses for each endpoint in the Odoo REST API module.

## Authentication

### Request Token

**Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "admin"}' http://localhost:8069/api/auth/token
```

**Response:**

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbGVzIjpbImFkbWluIl0sImV4cCI6MTYxNTI4OTk2OX0.2y2a-our0BZDm_I3kIq6a84MhVY7pwnhJ-8eC6AlyRk"
}
```

### Refresh Token

**Request:**

```bash
curl -X POST -H "Authorization: Bearer <your_token>" http://localhost:8069/api/auth/refresh
```

**Response:**

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbGVzIjpbImFkbWluIl0sImV4cCI6MTYxNTI4OTk2OX0.2y2a-our0BZDm_I3kIq6a84MhVY7pwnhJ-8eC6AlyRk"
}
```

## Webhooks

### Register Webhook

**Request:**

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <your_token>" -d '{"callback_url": "http://localhost:3000/callback"}' http://localhost:8069/api/webhooks
```

**Response:**

```json
{
  "message": "Webhook registered successfully."
}
```

## GraphQL Query

**Request:**

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <your_token>" -d '{"query": "{ user(id: 1) { name email } }"}' http://localhost:8069/api/graphql
```

**Response:**

```json
{
  "data": {
    "user": {
      "name": "Admin",
      "email": "admin@example.com"
    }
  }
}
```