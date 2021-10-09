from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lessons
from .serializers import ScheduleListSerializer


class ScheduleListView(APIView):
    """Выводит всё расписание конкретного ребёнка."""
    def get(self, request):
        schedule = Lessons.objects.all
        serializer = ScheduleListSerializer(schedule, many=True)
        return Response(serializer.data)
