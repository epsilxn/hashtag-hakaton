from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import *
from .models import *
from accounts.models import AdvancedUser


class ParentViewSet(viewsets.ModelViewSet):
    queryset = AdvancedUser.objects.filter(is_staff=False)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ParentSerializer


class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ChildSerializer

    # def create(self, request, *args, **kwargs):



