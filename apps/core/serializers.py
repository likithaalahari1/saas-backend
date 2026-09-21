from rest_framework import serializers
from .models import OAuthCredential, SocialAccount, Post, PostVariant, MediaAsset

class OAuthCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = OAuthCredential
        fields = '__all__'


class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = '__all__'


class PostVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVariant
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    variants_detail = PostVariantSerializer(source='variants', many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = '__all__'
