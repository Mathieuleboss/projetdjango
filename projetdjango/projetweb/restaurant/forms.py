from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employe', 'Employé'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Rôle")

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]