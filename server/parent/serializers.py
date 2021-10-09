from rest_framework import serializers
from .models import AdvancedUser, Child
from courses.serializers import AttendanceChildListSerializer


class ChildrenAttendanceSerializer(serializers.ModelSerializer):
    attendance_child = AttendanceChildListSerializer(many=True)

    class Meta:
        model = Child
        exclude = ["parent_of_child", "courses"]


class ParentSerializer(serializers.ModelSerializer):
    children_of_parent = ChildrenAttendanceSerializer(many=True)

    class Meta:
        model = AdvancedUser
        fields = ("id", "last_name", "first_name", "patronymic", "phone", "children_of_parent", "is_staff")
