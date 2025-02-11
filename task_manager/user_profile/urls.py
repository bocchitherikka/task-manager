from django.urls import path

from .views import profile_page

app_name = 'user_profile'

urlpatterns = [
    path('<slug:username>/', profile_page, name='profile_page'),
]
