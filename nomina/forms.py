from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import  User
from django.forms import ModelForm

class RegistroUsuario(UserCreationForm):
    username =forms.CharField(label='Usuario', max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})) 
    name = forms.CharField(label='Nombres', max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your name '}))
    last_name = forms.CharField(label='Apellidos', max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'}))
    email = forms.EmailField(label='Correo Electrónico', max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    class Meta:
        model = User
        fields = ('username', 'name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Quitando las validaciones predeterminadas
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.fields['password1'].widget=forms.TextInput(attrs={'placeholder': 'Enter your password '})
        self.fields['password2'].widget=forms.TextInput(attrs={'placeholder': 'Confirm your password '})
    
        
class CustomAuthenticationForm(AuthenticationForm):
    username =forms.CharField(label='Usuario', max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))


    