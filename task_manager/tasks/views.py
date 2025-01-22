from random import randint

from django.contrib.auth.decorators import login_required
from django.db.models import BooleanField, Value, Case, When
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import TaskForm
from .models import Task, User


@login_required
def index(request):
    template = 'index.html'
    tasks = Task.objects.filter(author=request.user)
    tasks = tasks.annotate(
        has_end_date=Case(
            When(end_date__isnull=False, then=Value(True)),
            default=Value(False),
            output_field=BooleanField()
        )
    )
    tasks = tasks.order_by('-has_end_date', 'end_date')
    context = {
        'tasks': tasks
    }
    return render(request, template, context)


@login_required
def add_task(request):
    template = 'add_task.html'
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task = form.save(commit=False)
        task.author = request.user
        contributors_usernames = form.clean_contributors()
        if contributors_usernames:
            for username in contributors_usernames:
                contributor = get_object_or_404(User, username=username)
                task.contributors.add(contributor)
        task.save()
        return redirect('tasks:main_page')
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def task_detail(request, task_id):
    template = 'task_detail.html'
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
    }
    return render(request, template, context)

