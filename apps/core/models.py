from django.db import models

PLATFORM_CHOICES = (
    ('instagram', 'Instagram'),
    ('facebook', 'Facebook'),
    ('linkedin', 'LinkedIn'),
    ('twitter', 'X (Twitter)'),
    ('tiktok', 'TikTok'),
    ('youtube', 'YouTube'),
    ('pinterest', 'Pinterest'),
)

POST_STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('in_review', 'In Review'),
    ('approved', 'Approved'),
    ('scheduled', 'Scheduled'),
    ('published', 'Published'),
    ('partially_published', 'Partially Published'),
    ('failed', 'Failed'),
)

class OAuthCredential(models.Model):
    """Stores developer OAuth API Client Keys & Secrets per platform."""
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES, unique=True)
    client_id = models.CharField(max_length=255, help_text="Meta App ID / Google Client ID / Twitter Key")
    client_secret = models.CharField(max_length=255, help_text="App Secret Key")
    redirect_uri = models.CharField(max_length=255, default='http://127.0.0.1:8000/api/oauth/callback/')
    developer_key = models.CharField(max_length=255, blank=True, null=True, help_text="YouTube API key / Bearer token")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_platform_display()} Credentials"


class SocialAccount(models.Model):
    """Connected user social channel with OAuth tokens."""
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES)
    account_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    avatar_url = models.URLField(max_length=500, blank=True, null=True)
    is_connected = models.BooleanField(default=True)
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    token_expires_at = models.DateTimeField(blank=True, null=True)
    followers_count = models.IntegerField(default=0)
    posts_published_count = models.IntegerField(default=0)
    health = models.CharField(max_length=20, default='healthy')
    last_synced = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account_name} ({self.username}) [{self.platform}]"


class Post(models.Model):
    """Multi-channel post object."""
    global_caption = models.TextField()
    global_media_urls = models.JSONField(default=list)
    platforms = models.JSONField(default=list)
    status = models.CharField(max_length=30, choices=POST_STATUS_CHOICES, default='draft')
    scheduled_at = models.DateTimeField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by_name = models.CharField(max_length=100, default='Likitha Sri')

    def __str__(self):
        return f"Post #{self.id}: {self.global_caption[:30]}..."


class PostVariant(models.Model):
    """Per-platform customized copy and media overrides."""
    post = models.ForeignKey(Post, related_name='variants', on_delete=models.CASCADE)
    platform = models.CharField(max_length=30, choices=PLATFORM_CHOICES)
    caption = models.TextField(blank=True)
    hashtags = models.JSONField(default=list)
    custom_options = models.JSONField(default=dict)
    status = models.CharField(max_length=20, default='pending')
    error_message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.post.id} - {self.platform}"


class MediaAsset(models.Model):
    """Media library upload asset."""
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=500)
    asset_type = models.CharField(max_length=20, default='image')
    dimensions = models.CharField(max_length=50, default='1920 x 1080')
    size_bytes = models.IntegerField(default=1500000)
    folder = models.CharField(max_length=100, default='Campaign Assets')
    tags = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
