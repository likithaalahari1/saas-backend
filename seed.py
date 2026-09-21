import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socially_backend.settings')
django.setup()

from apps.core.models import OAuthCredential, SocialAccount, Post, MediaAsset

# Seed OAuth Developer Credentials for Meta, Google, LinkedIn, Twitter, TikTok, Pinterest
platforms = [
    ('instagram', 'meta_app_id_948201', 'meta_app_secret_8492048', 'http://127.0.0.1:8000/api/oauth/callback/instagram/'),
    ('facebook', 'meta_app_id_948201', 'meta_app_secret_8492048', 'http://127.0.0.1:8000/api/oauth/callback/facebook/'),
    ('youtube', 'google_client_id_48201.apps.googleusercontent.com', 'google_client_secret_94820', 'http://127.0.0.1:8000/api/oauth/callback/youtube/'),
    ('linkedin', 'linkedin_client_id_84920', 'linkedin_client_secret_20194', 'http://127.0.0.1:8000/api/oauth/callback/linkedin/'),
    ('twitter', 'twitter_client_id_48201', 'twitter_client_secret_94021', 'http://127.0.0.1:8000/api/oauth/callback/twitter/'),
    ('tiktok', 'tiktok_client_key_84920', 'tiktok_client_secret_2019', 'http://127.0.0.1:8000/api/oauth/callback/tiktok/'),
    ('pinterest', 'pinterest_app_id_48201', 'pinterest_app_secret_9401', 'http://127.0.0.1:8000/api/oauth/callback/pinterest/'),
]

for p, cid, csecret, ruri in platforms:
    OAuthCredential.objects.update_or_create(
        platform=p,
        defaults={
            'client_id': cid,
            'client_secret': csecret,
            'redirect_uri': ruri,
            'is_active': True
        }
    )

print("SUCCESS: Django database seeded with OAuth Developer credentials for Meta, Google/YouTube, Twitter, LinkedIn, TikTok, and Pinterest!")
