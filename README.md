# Socially SaaS Django REST Backend

Unified Social Media Management Studio - Django REST Framework Backend API.

## Features

- **OAuth 2.0 Credential Management**: Encrypted storage for Meta (Instagram/Facebook), Google/YouTube, LinkedIn, Twitter/X, TikTok, and Pinterest App Keys & Client Secrets.
- **Authentic OAuth Authorization Redirects**: API endpoints to generate authorization URLs for all 7 platforms.
- **Multi-Platform Publisher Runner**: Background and real-time execution engine to publish posts across networks.
- **REST Endpoints**:
  - `GET / POST /api/credentials/` - Manage platform API Client IDs & Secrets.
  - `GET / POST /api/accounts/` - Manage connected channels and OAuth tokens.
  - `GET /api/oauth/authorize/<platform>/` - Fetch OAuth redirect URLs.
  - `GET / POST /api/posts/` - Multi-channel post creation.
  - `POST /api/posts/<id>/publish/` - Trigger simultaneous multi-platform publishing.

## Getting Started

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Run database migrations:
   ```bash
   python manage.py migrate
   ```

3. Seed OAuth developer credentials:
   ```bash
   python seed.py
   ```

4. Start Django REST server:
   ```bash
   python manage.py runserver 8000
   ```
