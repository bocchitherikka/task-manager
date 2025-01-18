from django.db import models


default = 0
TASK_STATUS_CHOICES = [
    ('IP', 'In Progress'),
    ('COM', 'Completed'),
    ('PP', 'Postponed'),
    ('DR', 'Dropped'),
    ('CAN', 'Cancelled')
]


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    status = models.CharField(
        choices=TASK_STATUS_CHOICES,
        default=TASK_STATUS_CHOICES[default],
        max_length=16
    )
    date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
