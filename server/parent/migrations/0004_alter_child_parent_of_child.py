# Generated by Django 3.2.8 on 2021-10-08 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parent', '0003_alter_parentuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent_of_child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_of_parent', to=settings.AUTH_USER_MODEL, verbose_name='Родитель'),
        ),
    ]
