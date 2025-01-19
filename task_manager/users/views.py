from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('tasks:main_page')
    template_name = 'signup.html'


class Login(LoginView):
    success_url = reverse_lazy('tasks:main_page')
    template_name = 'login.html'


class Logout(LogoutView):
    template_name = 'logout.html'

