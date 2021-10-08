from .models import Teacher, Courses
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import *


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoursesSerializer

    def get_queryset(self):
        """
        Переопределяется для того, чтобы при попытке сделать PUT/DELETE не выкидывало 404
        :return:
        """
        if self.request.method == "PUT" or self.request.method == "DELETE":
            return Courses.objects.all()
        else:
            return Courses.objects.filter(is_deleted=False)


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonsSerializer
