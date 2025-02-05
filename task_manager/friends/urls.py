from django.urls import path, re_path

from .views import (
    delete_friendship,
    process_friendship_request,
    send_friendship_request
)

app_name = 'friends'

urlpatterns = [
    path(
        'delete/<int:user_id>/',
        delete_friendship,
        name='delete_friendship'
    ),
    path(
        'add/<int:user_id>/',
        send_friendship_request,
        name='send_request'
    ),
    re_path(
        r'^(?P<action>accept|reject)/(?P<user_id>\d+)',
        process_friendship_request,
        name='process_request'
    )
]
