from .models import ParentUser, Child
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import ParentSerializer


class ParentViewSet(viewsets.ModelViewSet):
    queryset = ParentUser.objects.all()

    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = ParentSerializer



