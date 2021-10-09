from rest_framework import serializers
from .models import *
from accounts.models import AdvancedUser
from parent.serializers import ChildrenSerializer
from djoser.conf import settings


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvancedUser
        fields = tuple(AdvancedUser.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        )
        # exclude = ["password", "is_superuser", "is_staff", "is_active",
        #            "date_joined", "last_login", "groups", "user_permissions"]


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    lessons_in_course = LessonsSerializer(many=True)

    class Meta:
        model = Courses
        fields = "__all__"


# class TeacherOneSerializer(serializers.ModelSerializer):
#     teacher_course = CoursesSerializer(many=True)
#
#     class Meta:
#         model = AdvancedUser
#         exclude = ["password", "is_superuser", "is_staff", "is_active",
#                    "date_joined", "last_login", "groups", "user_permissions"]


class CoursesManySerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = "__all__"


# class ScheduleListSerializer(serializers.ModelSerializer):
#     """Расписание"""
#     class Meta:
#         model = Lessons
#         fields = "__all__"


class ScheduleListSerializer(serializers.ModelSerializer):
    """Расписание по ID ребёнка"""
    schedule_lessons = LessonsSerializer(many=True)
    schedule_child = ChildrenSerializer(many=True)

    class Meta:
        model = Attendance
        fields = "__all__"


class AttendanceListSerializer(serializers.ModelSerializer):
    """comm"""
    class Meta:
        model = Attendance
        fields = "__all__"
