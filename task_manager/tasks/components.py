from django.db.models import (
    BooleanField, Case, Q, QuerySet, Value, When
)
from django.http import HttpRequest
from typing import Optional

from .models import Task, User


def order_tasks_by_end_date(
        tasks: QuerySet[Task]
) -> QuerySet[Task]:
    tasks = tasks.annotate(
        has_end_date=Case(
            When(end_date__isnull=False, then=Value(True)),
            default=Value(False),
            output_field=BooleanField()
        )
    )
    tasks = tasks.order_by('-has_end_date', 'end_date')
    return tasks


def get_request_user_tasks(
        request: HttpRequest
) -> QuerySet[Task]:
    tasks = Task.objects.filter(
        Q(author=request.user) | Q(contributors=request.user)
    )
    return tasks


def filter_tasks_by_status(
        tasks: QuerySet[Task],
        status: Optional[str]
) -> QuerySet[Task]:
    if status:
        tasks = tasks.filter(status=status)
    return tasks
