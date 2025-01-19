from django.urls import path

from .views import Login, Logout, SignUp


app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        Logout.as_view(),
        name='logout'
    ),
    path(
        'signup/',
        SignUp.as_view(),
        name='signup'
    ),
    path(
        'login/',
        Login.as_view(),
        name='login'
    ),
]