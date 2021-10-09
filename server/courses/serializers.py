from rest_framework import serializers
from .models import *
from accounts.models import AdvancedUser
from djoser.conf import settings


class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        exclude = ["parent_of_child", "courses"]


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvancedUser
        fields = tuple(AdvancedUser.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
        )
        # exclude = ["password", "is_superuser", "is_staff", "is_active",
        #            "date_joined", "last_login", "groups", "user_permissions"]


class AttendanceChildListSerializer(serializers.ModelSerializer):
    """Расписание по ID ребёнка"""

    class Meta:
        model = Attendance
        exclude = ["child"]


class AttendanceLessonListSerializer(serializers.ModelSerializer):
    """Посещение по занятиям"""
    class Meta:
        model = Attendance
        exclude = ["lesson"]


class LessonsSerializer(serializers.ModelSerializer):
    attendance_lessons = AttendanceLessonListSerializer(many=True)

    class Meta:
        model = Lessons
        fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    lessons_in_course = LessonsSerializer(many=True)
    children_of_courses = ChildrenSerializer(many=True)

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