from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from .models import AdvancedUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = AdvancedUser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
