from random import randint

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .components import (
    add_contributors_to_task,
    filter_tasks_by_status,
    get_request_user_tasks,
    order_tasks_by_end_date,
    request_user_is_has_access,
    save_task_form
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
        save_task_form(form, request)
        url = reverse('tasks:main_page') + '?status=in_progress'
        return redirect(url)

    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def task_detail(request, task_id):
    template = 'task_detail.html'
    edit = request.GET.get('edit', False)
    task = get_object_or_404(Task, pk=task_id)

    if not request_user_is_has_access(request, task, edit):
        return render(request, 'access_denied.html')

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        contributors_usernames = form.clean_contributors()
        add_contributors_to_task(task, contributors_usernames)
        return redirect('tasks:task_detail', task_id=task_id)

    context = {
        'form': form,
        'task': task,
        'edit': edit,
        'user': request.user

    }
    return render(request, template, context)

