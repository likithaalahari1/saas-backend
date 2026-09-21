from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OAuthCredentialViewSet, 
    SocialAccountViewSet, 
    PostViewSet, 
    MediaAssetViewSet,
    get_oauth_authorize_url,
    oauth_callback,
    health_check
)

router = DefaultRouter()
router.register(r'credentials', OAuthCredentialViewSet, basename='credential')
router.register(r'accounts', SocialAccountViewSet, basename='account')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'media', MediaAssetViewSet, basename='media')

urlpatterns = [
    path('health/', health_check, name='health-check'),
    path('oauth/authorize/<str:platform>/', get_oauth_authorize_url, name='oauth-authorize-url'),
    path('oauth/callback/<str:platform>/', oauth_callback, name='oauth-callback'),
    path('', include(router.urls)),
]

