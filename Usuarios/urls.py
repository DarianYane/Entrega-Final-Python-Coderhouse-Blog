from re import template
from django.urls import path
from Usuarios import views
from Usuarios.views import UserRegisterView, UserEditView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
     path ('register/', UserRegisterView.as_view(), name = 'register'),
     path ('editar/', UserEditView.as_view(), name = 'edit_profile'),
     path ('password/', auth_views.PasswordChangeView.as_view(template_name='registration/password.html')),  

]