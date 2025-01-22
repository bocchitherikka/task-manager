from django.urls import path

from .views import add_task, index

app_name = 'tasks'

urlpatterns = [
    path('', index, name='main_page'),
    path('add/', add_task, name='add_task'),
]