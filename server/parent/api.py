from rest_framework import viewsets, permissions
from .serializers import *
from .models import *
from accounts.models import AdvancedUser
from courses.models import Courses, Lessons, Attendance
from rest_framework.response import Response


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
        new_child = Child.objects.create(last_name=child_data["last_name"], first_name=child_data["first_name"],
                                         patronymic=child_data["patronymic"],
                                         parent_of_child=curr_parent, courses=curr_course)
        new_child.save()
        serializer = ChildSerializer(new_child)
        all_lessons = Lessons.objects.filter(course=curr_course)
        for one_lesson in all_lessons:
            new_attend = Attendance.objects.create(child=new_child, lesson=one_lesson)
            new_attend.save()
        return Response(serializer.data)


    # def create(self, request, *args, **kwargs):



