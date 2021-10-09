from rest_framework import serializers
from .models import AdvancedUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvancedUser
        exclude = ["password", ]
