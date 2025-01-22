from django.urls import path

from .views import add_task, index, task_detail

app_name = 'tasks'

urlpatterns = [
    path('', index, name='main_page'),
    path('add/', add_task, name='add_task'),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
]