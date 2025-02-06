from django.urls import path, re_path

from .views import (
    delete_friendship,
    process_friendship_request,
    send_friendship_request
)

app_name = 'friends'

urlpatterns = [
    path(
        'delete/<slug:username>/',
        delete_friendship,
        name='delete_friendship'
    ),
    path(
        'add/<slug:username>/',
        send_friendship_request,
        name='send_request'
    ),
    re_path(
        r'^(?P<action>accept|reject)/(?P<username>[\w-]+)',
        process_friendship_request,
        name='process_request'
    )
]
