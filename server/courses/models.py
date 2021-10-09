from django.db import models
from parent.models import Child
from accounts.models import AdvancedUser

# class Teacher(models.Model):
#     email = models.EmailField(verbose_name="Почта", unique=True)
#     password = models.TextField(verbose_name="Пароль")
#     first_name = models.CharField(max_length=32, verbose_name="Имя")
#     last_name = models.CharField(max_length=32, verbose_name="Фамилия")
#     patronymic = models.CharField(max_length=32, verbose_name="Отчество")
#
#     class Meta:
#         verbose_name = "Преподаватель"
#         verbose_name_plural = "Преподаватели"
#
#     def __str__(self):
#         return self.email


class Courses(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назание курса")
    description = models.TextField(verbose_name="Описание курса")
    teacher = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE,
                                verbose_name="Преподаватель", related_name="teacher_course")
    is_deleted = models.BooleanField(verbose_name="Удален", default=False)
    emoji = models.CharField(max_length=255, verbose_name="Emoji", default="😀")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

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

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def __str__(self):
        return str(f"{self.course.name} {self.id}")


class Attendance(models.Model):
    """Класс реализует модель для сущности 'Посещаемость'."""
    paid_confirmed_parent = models.BooleanField(default=False, blank=True,
                                                verbose_name="Родитель подтвердил оплату")
    paid_confirmed_teacher = models.BooleanField(default=False, blank=True,
                                                 verbose_name="Преподаватель подтвердил оплату")
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name="Занятие")

    class Meta:
        verbose_name = "Посещаемость ученика"
        verbose_name_plural = "Посещаемость учеников"