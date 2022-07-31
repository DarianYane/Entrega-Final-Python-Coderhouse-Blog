from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import is_valid_path
from Usuarios.forms import UserRegisterForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')