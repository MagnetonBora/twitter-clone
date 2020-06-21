from rest_framework import serializers
from .models import Status, AppUser


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = [
            'id', 'url', 'screen_name', 'name', 'location', 'description',
            'verified', 'profile_banner', 'profile_image', 'followers', 'following'    
        ]


class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id', 'url', 'user', 'created_at', 'text', 'favourited', 
            'reply_to', 'quoted_status', 'retweeted_status', 'entities' 
        ]