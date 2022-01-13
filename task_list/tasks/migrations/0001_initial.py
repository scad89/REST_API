# Generated by Django 3.2.4 on 2022-01-13 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50, verbose_name='Task Name')),
                ('day_of_week', models.CharField(choices=[('Monday', 'Mon'), ('Tuesday', 'Tue'), ('Wednesday', 'Wed'), ('Thursday', 'Thu'), ('Friday', 'Fri'), ('Saturday', 'Sat'), ('Sunday', 'Sun')], default='SUN', max_length=9)),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('comment', models.CharField(blank=True, max_length=100, verbose_name='Comment')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('id_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
