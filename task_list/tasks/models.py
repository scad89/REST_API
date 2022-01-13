from django.contrib.auth.models import User
from django.db import models


class TaskTable(models.Model):
    class Day(models.TextChoices):
        MON = 'Monday'
        TUE = 'Tuesday'
        WED = 'Wednesday'
        THU = 'Thursday'
        FRI = 'Friday'
        SAT = 'Saturday'
        SUN = 'Sunday'

    task_name = models.CharField('Task Name', max_length=50)
    day_of_week = models.CharField(
        choices=Day.choices, max_length=9, default='SUN')
    date = models.DateTimeField(
        'Date', auto_now_add=False, null=True)
    comment = models.CharField('Comment', max_length=100, blank=True)
    id_user = models.ForeignKey(
        User, related_name='user', on_delete=models.CASCADE, null=True, verbose_name='User')
    enabled = models.BooleanField('Enabled', default=False)

    def __str__(self):
        return self.task_name

    class Meta:
        verbose_name = 'Task Table'
        verbose_name_plural = 'Task Tables'
