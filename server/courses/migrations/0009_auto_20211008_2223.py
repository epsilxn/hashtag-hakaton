# Generated by Django 3.2.8 on 2021-10-08 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_auto_20211008_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
