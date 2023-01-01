from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView,
                                       PasswordChangeView, PasswordChangeDoneView)

# Create your views here.


class RegisterPage(CreateView):
    form_class = RegistrationForm
    template_name = 'access/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)


class LandingPage(TemplateView):
    template_name = 'access/landingpage.html'


class LoginPage(LoginView):
    template_name = 'access/login.html'


class LogoutPage(LogoutView):
    template_name = 'access/logout.html'

class ResetPasswordPage(PasswordResetView):
    template_name = 'access/password-reset.html'

class ChangePasswordPage(PasswordChangeView):
    template_name = 'access/password-change.html'