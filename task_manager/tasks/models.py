from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
default = 0
TASK_STATUS_CHOICES = [
    ('IP', 'Выполняется'),
    ('COM', 'Выполнено'),
    ('PP', 'Отложено'),
    ('DR', 'Брошено'),
    ('CAN', 'Отменено')
]


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owned_tasks'
    )
    contributors = models.ManyToManyField(
        User,
        related_name='participating_tasks',
        blank=True
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    status = models.CharField(
        choices=TASK_STATUS_CHOICES,
        default=TASK_STATUS_CHOICES[default],
        max_length=16
    )
    date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
