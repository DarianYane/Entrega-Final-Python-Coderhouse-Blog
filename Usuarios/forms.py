from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} #Saca los mensajes de ayuda
    
   

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, label='Nombre', widget=forms.TextInput)
    last_name = forms.CharField(max_length=100, label='Apellido', widget=forms.TextInput)
    username = forms.CharField(max_length=100, label='Nombre de Usuario',widget=forms.TextInput)
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email']
   