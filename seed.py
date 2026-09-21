import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socially_backend.settings')
django.setup()

from apps.core.models import OAuthCredential, SocialAccount, Post, MediaAsset

# Seed OAuth Developer Credentials for Meta, Google, LinkedIn, Twitter, TikTok, Pinterest
platforms = [
    ('instagram', '1767475414295181', '7e166a19b2c14e76fc672b79a0c23b51', 'https://andhrayatri.in/api/oauth/callback/instagram/'),
    ('facebook', '1767475414295181', '7e166a19b2c14e76fc672b79a0c23b51', 'https://andhrayatri.in/api/oauth/callback/facebook/'),
    ('youtube', 'google_client_id_48201.apps.googleusercontent.com', 'google_client_secret_94820', 'https://andhrayatri.in/api/oauth/callback/youtube/'),
    ('linkedin', 'linkedin_client_id_84920', 'linkedin_client_secret_20194', 'https://andhrayatri.in/api/oauth/callback/linkedin/'),
    ('twitter', 'twitter_client_id_48201', 'twitter_client_secret_94021', 'https://andhrayatri.in/api/oauth/callback/twitter/'),
    ('tiktok', 'tiktok_client_key_84920', 'tiktok_client_secret_2019', 'https://andhrayatri.in/api/oauth/callback/tiktok/'),
    ('pinterest', 'pinterest_app_id_48201', 'pinterest_app_secret_9401', 'https://andhrayatri.in/api/oauth/callback/pinterest/'),
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
