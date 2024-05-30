from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['data', 'hora', 'numero_pessoas', 'observacoes']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']