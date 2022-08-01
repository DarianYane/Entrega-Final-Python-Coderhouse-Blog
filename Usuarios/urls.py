from django.urls import path
from Usuarios import views
from Usuarios.views import UserRegisterView, UserEditView
from django.contrib.auth.views import LogoutView



urlpatterns = [
     path ('register/', UserRegisterView.as_view(), name = 'register'),
     path ('editar/', UserEditView.as_view(), name = 'edit_profile'),  

]