from django.shortcuts import render
from api.serializers import User, UserSerializer
from rest_framework import viewsets
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer