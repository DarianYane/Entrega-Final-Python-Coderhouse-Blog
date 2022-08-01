from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.urls import is_valid_path
from Usuarios.forms import EditProfileForm, UserRegisterForm
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editar_usuario.html'
    success_url = reverse_lazy('bienvenida')

    def get_object(self):
        return self.request.user

