from .serializers import AppUser, UserSerializer, Status, StatusSerializer, StatusCreateSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer
    

class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Status.objects.order_by('-created_at')
    serializer_class = StatusCreateSerializer

    action_serializers = {
        'retrieve': StatusSerializer,
        'create': StatusCreateSerializer,
        'list': StatusSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(StatusViewSet, self).get_serializer_class()
