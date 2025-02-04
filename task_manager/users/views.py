from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import CreationForm


class RedirectAuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('tasks:main_page')
        return super().dispatch(request, *args, **kwargs)


class SignUp(RedirectAuthenticatedMixin, CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('tasks:main_page')
    template_name = 'signup.html'


class Login(RedirectAuthenticatedMixin, LoginView):
    success_url = reverse_lazy('tasks:main_page')
    template_name = 'login.html'


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('users:login')
        return super().dispatch(request, *args, **kwargs)
