from random import randint

from django.contrib.auth.decorators import login_required
from django.db.models import BooleanField, Value, Case, When, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .components import (
    filter_tasks_by_status,
    get_request_user_tasks,
    order_tasks_by_end_date
)
from .forms import TaskForm
from .models import Task, User


@login_required
def main_page(request):
    template = 'main_page.html'
    tasks = get_request_user_tasks(request)
    status = request.GET.get('status')
    tasks = filter_tasks_by_status(tasks, status)
    tasks = order_tasks_by_end_date(tasks)
    context = {
        'tasks': tasks,
        'status': status
    }
    return render(request, template, context)


@login_required
def add_task(request):
    template = 'add_task.html'
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        task.save()
        contributors_usernames = form.clean_contributors()
        for username in contributors_usernames:
            contributor = get_object_or_404(User, username=username)
            task.contributors.add(contributor)
        task.save()
        return redirect(reverse('tasks:main_page') + '?status=in_progress')
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def task_detail(request, task_id):
    template = 'task_detail.html'
    edit = request.GET.get('edit', False)
    task = get_object_or_404(Task, pk=task_id)
    user = request.user
    contributors = task.contributors.all()
    if user != task.author and user not in contributors:
        return render(
            request,
            'access_denied.html',
            {'casino': randint(1, 1000)}
        )
    form = TaskForm(
        request.POST or None,
        instance=task
    )
    if form.is_valid():
        contributors_usernames = form.clean_contributors()
        if contributors_usernames:
            for username in contributors_usernames:
                contributor = get_object_or_404(User, username=username)
                if contributor not in task.contributors.all():
                    task.contributors.add(contributor)
        task.save()
        return redirect('tasks:task_detail', task_id=task_id)
    context = {
        'form': form,
        'task': task,
        'edit': edit
    }
    return render(request, template, context)

