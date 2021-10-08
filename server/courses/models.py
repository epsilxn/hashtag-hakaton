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
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    is_deleted = models.BooleanField(verbose_name="Удален", default=False)
    emoji = models.CharField(max_length=255, verbose_name="Emoji", default="😀")

    def __str__(self):
        return str(self.id)


class Lessons(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название занятия")
    description = models.TextField(verbose_name="Описание занятия")
    date = models.DateField(verbose_name="Дата занятия")
    time = models.TimeField(verbose_name="Время занятия")
    information = models.TextField(verbose_name="Информация о занятии")
    # Название у Lessons.course - lessons_in_course. BE CAREFUL!
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name="Курс", related_name="lessons_in_course")

    def __str__(self):
        return str(f"{self.course.name} {self.id}")
