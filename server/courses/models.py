from django.db import models


class Teacher(models.Model):
    email = models.EmailField(verbose_name="Почта", unique=True)
    password = models.TextField(verbose_name="Пароль")
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=32, verbose_name="Отчество")

    def __str__(self):
        return self.email


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назание курса")
    description = models.TextField(verbose_name="Описание курса")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="Преподаватель")
    is_deleted = models.BooleanField(verbose_name="Удален", default=False)

    def __str__(self):
        return self.id
