from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import TaskForm
from .models import Task


@login_required
def index(request):
    template = 'index.html'
    tasks = Task.objects.all()
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
        contributors = form.clean_contributors()
        if contributors:
            task.contributors.add(*contributors)
        task.save()
        return redirect('tasks:main_page')
    context = {
        'form': form,
    }
    return render(request, template, context)
