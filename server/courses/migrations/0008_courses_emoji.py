# Generated by Django 3.2.7 on 2021-10-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_courses_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='emoji',
            field=models.CharField(default='', max_length=255, verbose_name='Emoji'),
        ),
    ]
