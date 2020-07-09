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
    user = UserSerializer()
    quoted_status = serializers.SerializerMethodField()
    retweeted_status = serializers.SerializerMethodField()
    reply_to = serializers.SerializerMethodField()
    retweet_count = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()
    favourite_count = serializers.SerializerMethodField()

    class Meta:
        model = Status
        fields = [
            'id', 'url', 'user', 'created_at', 'text', 'favourited', 
            'reply_to', 'quoted_status', 'retweeted_status', 'entities',
            'retweet_count', 'reply_count', 'favourite_count'
        ]

    def get_quoted_status(self, obj):
        if obj.quoted_status:
            return StatusSerializer(obj.quoted_status, context=self.context).data
        return None

    def get_retweeted_status(self, obj):
        if obj.retweeted_status:
            return StatusSerializer(obj.retweeted_status, context=self.context).data
        return None
    
    def get_reply_to(self, obj):
        if obj.reply_to:
            return StatusSerializer(obj.reply_to, context=self.context).data
        return None

    def get_retweet_count(self, obj):
        return obj.quotations.count()

    def get_reply_count(self, obj):
        return obj.replies.count()

    def get_favourite_count(self, obj):
        return obj.favourited.count()

    # def create(self, validated_data):
    #     validated_data.pop('favourited')
    #     validated_data.pop('entities')
    #     return Status.objects.create(**validated_data)

    
class StatusCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = [
            'id', 'user', 'created_at', 'text', 'reply_to', 'quoted_status', 'retweeted_status', 'entities',
        ]