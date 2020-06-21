from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
import uuid
from .managers import AppUserManager

# Create your models here.
class AppUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    screen_name = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=240, null=True, blank=True)
    verified = models.BooleanField(default=False)
    followers = models.ManyToManyField('AppUser', related_name='followers_users', related_query_name='followers_users')  # users who are following a user
    following = models.ManyToManyField('AppUser', related_name='following_users', related_query_name='following_users')  # users who are followed by a user
    profile_banner = models.ImageField()
    profile_image = models.ImageField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'screen_name'
    REQUIRED_FIELDS = ['name', 'email']

    objects = AppUserManager()

    def __str__(self):
        return f'User {self.name}(@{self.screen_name})'
    

class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    favourited = models.ManyToManyField(AppUser, related_name='favourites_statuses', blank=True)
    reply_to = models.ManyToManyField('Status', blank=True, related_name='replies')
    quoted_status = models.ManyToManyField('Status', blank=True, related_name='quotations')
    retweeted_status = models.ManyToManyField('Status', blank=True, related_name='retweets')
    entities = models.ManyToManyField('Entities', blank=True)

    def __str__(self):
        return f'Tweet created by {self.user} @ {self.created_at}'
    
class Entities(models.Model):
    pass