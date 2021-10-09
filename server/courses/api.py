from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import *
from accounts.models import AdvancedUser


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = AdvancedUser.objects.filter(is_staff=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializer

    # def get_queryset(self):
    #     try:
    #         teacher_id = int(self.kwargs["pk"])
    #         teacher = AdvancedUser.objects.filter(id=teacher_id, is_staff=True)
    #         result = TeacherOneSerializer(teacher, many=True)
    #         return result
    #     except Exception as e:
    #         print(e)
    #         return AdvancedUser.objects.filter(is_staff=True)


class CourseForTeacherViewSet(viewsets.ModelViewSet):
    ...


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoursesManySerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Если пингуется по пути /api/course/id, то возвращаться будет с полем lessons_in_course
        """
        pk = int(kwargs["pk"])
        queryset = Courses.objects.filter(id=pk)
        serializer = CoursesSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        """
        Переопределяется для того, чтобы при попытке сделать PUT/DELETE не выкидывало 404
        :return:
        """
        # print(self.request.query_params["name"])
        if self.request.method == "PUT" or self.request.method == "DELETE":
            return Courses.objects.all()
        else:
            try:
                return Courses.objects.filter(is_deleted=False, teacher_id=int(self.request.query_params["id"]))
            except Exception as e:
                return Courses.objects.filter(is_deleted=False)


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonsSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    """Расписание по ID ребёнка."""
    queryset = Attendance.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttendanceListSerializer

    def retrieve(self, request, *args, **kwargs):
        """"""
        pk = int(kwargs["pk"])
        self.queryset = self.queryset.objects.filter(child=pk)
        # queryset = Courses.objects.filter(id=pk)
        serializer = ScheduleListSerializer(self.queryset, many=True)
        return Response(serializer.data)