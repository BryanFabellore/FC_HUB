from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.http import HttpResponse
from django.template import loader
from django.db import models
from accounts.models import user_acc
from .forms import user_accForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
# Create your views here.


class LoginInterfaceView(LoginView):
    template_name = 'login/log_in.html'
    



class UserCreateView(CreateView):
    model = user_acc
    success_url = '/'
    form_class = user_accForm
    template_name = 'login/signup.html'

