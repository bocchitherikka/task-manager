from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Task


def index(request):
    template = 'index.html'
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, template, context)
