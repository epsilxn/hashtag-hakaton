from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvancedUser(AbstractUser):
    """Класс реализует модель для сущности 'Пользователь'."""
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    phone = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

