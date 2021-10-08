from django.contrib import admin
from .models import Courses, Teacher


class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    search_fields = ("id", )


admin.site.register(Courses, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
