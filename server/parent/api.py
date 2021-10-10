from rest_framework.response import Response
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from courses.models import Courses, Lessons, Attendance
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

    def create(self, request, *args, **kwargs):
        child_data = request.data
        curr_parent = AdvancedUser.objects.get(id=child_data["parent_of_child"])
        curr_course = Courses.objects.get(id=child_data["courses"])
        new_child = Child(last_name=child_data["last_name"], first_name=child_data["first_name"],
                          patronymic=child_data["patronymic"],
                          parent_of_child=curr_parent)
        new_child.save()
        new_child.courses.add(curr_course)
        new_child.save()
        all_lessons = Lessons.objects.filter(course=curr_course.id)
        for one_lesson in all_lessons:
            Attendance.objects.create(child=new_child, lesson=one_lesson).save()
        serializer = ChildSerializer(new_child)
        return Response(serializer.data)



