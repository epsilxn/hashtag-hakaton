from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    search_fields = ("id", )


class LessonsAdmin(admin.ModelAdmin):
    list_display = ("id", )
    search_fields = ("id",)


admin.site.register(Courses, CourseAdmin)
# admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Attendance)
