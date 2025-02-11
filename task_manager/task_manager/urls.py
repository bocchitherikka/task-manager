from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        '',
        include('tasks.urls', namespace='tasks')
    ),
    path(
        'auth/',
        include('users.urls', namespace='users')
    ),
    path(
        'friends/',
        include('friends.urls', namespace='friends')
    ),
    path(
        'profile/',
        include('user_profile.urls', namespace='profile')
    ),
    path(
        'admin/',
        admin.site.urls
    )
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
