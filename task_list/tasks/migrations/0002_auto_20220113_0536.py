# Generated by Django 3.2.4 on 2022-01-13 02:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskModel',
            new_name='TaskTable',
        ),
        migrations.AlterModelOptions(
            name='tasktable',
            options={'verbose_name': 'Task Table', 'verbose_name_plural': 'Task Tables'},
        ),
    ]
