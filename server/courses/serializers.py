from rest_framework import serializers
from .models import *
from accounts.models import AdvancedUser


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvancedUser
        exclude = ["password", ]


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = "__all__"


class CoursesSerializer(serializers.ModelSerializer):
    lessons_in_course = LessonsSerializer(many=True)

    class Meta:
        model = Courses
        fields = "__all__"


class CoursesManySerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = "__all__"


class ScheduleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lessons
        fields = "__all__"