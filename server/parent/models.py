from django.db import models
from accounts.models import AdvancedUser


class BaseModel(models.Model):
    """Базовый класс для моделей, которые наследуются от 'models.Model'."""
    objects = models.Manager()

    class Meta:
        abstract = True


class Child(BaseModel):
    """Класс реализует модель для сущности 'Дети'."""
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    parent_of_child = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE, verbose_name="Родитель",
                                        related_name="children_of_parent")
    courses = models.ManyToManyField("courses.Courses", verbose_name="Курсы", related_name="children_of_courses")

    class Meta:
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"
