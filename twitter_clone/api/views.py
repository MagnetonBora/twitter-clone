from django.shortcuts import render
from .serializers import AppUser, UserSerializer, Status, StatusSerializer
from rest_framework import viewsets
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


# ViewSets define the view behavior.
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer