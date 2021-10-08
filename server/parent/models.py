from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    """Базовый класс для моделей, которые наследуются от 'models.Model'."""
    objects = models.Manager()

    class Meta:
        abstract = True


class ParentUser(AbstractUser):
    """Класс реализует модель для сущности 'Родители'."""
    patronymic = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"


class Child(BaseModel):
    """Класс реализует модель для сущности 'Дети'."""
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    parent_of_child = models.ForeignKey(ParentUser, on_delete=models.CASCADE, verbose_name="Родитель",
                                        related_name="children_of_parent")

    class Meta:
        verbose_name = "Ребёнок"
        verbose_name_plural = "Дети"
