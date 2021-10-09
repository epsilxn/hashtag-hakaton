from rest_framework import serializers
from .models import AdvancedUser, Child


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        exclude = ["parent_of_child", "courses"]


class ParentSerializer(serializers.ModelSerializer):
    children_of_parent = ChildrenSerializer(many=True)

    class Meta:
        model = AdvancedUser
        fields = ("id", "last_name", "first_name", "patronymic", "phone", "children_of_parent")

