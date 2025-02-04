from django.db.models import (
    BooleanField, Case, Q, QuerySet, Value, When
)
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from typing import Optional

from .forms import TaskForm
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


def add_contributors_to_task(
        task: Task,
        contributors_usernames: list[User]
) -> Task:
    for username in contributors_usernames:
        contributor = get_object_or_404(User, username=username)
        task.contributors.add(contributor)
    task.save()
    return task


def save_task_form(
        form: TaskForm,
        request: HttpRequest
) -> Task:
    task = form.save(commit=False)
    task.author = request.user
    task.save()
    contributors_usernames = form.clean_contributors()
    add_contributors_to_task(task, contributors_usernames)
    return task


def request_user_is_has_task_access(
        request: HttpRequest,
        task: Task,
        edit: Optional[str]
) -> bool:
    user = request.user
    contributors = task.contributors.all()
    if (
        user != task.author and
        user not in contributors or
        user != task.author and
        user in contributors and
        edit
    ):
        return False
    return True
