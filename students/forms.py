from .models import Student
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone_number', 'course', 'description' ,'image']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username cannot exceed 150 characters.'
        }
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}),
        error_messages={'required': 'Email is required.'}
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        help_text=(
            "Password must be at least 8 characters long, include at least one uppercase letter, "
            "one lowercase letter, one number, and one special character."
        ),
        error_messages={'required': 'Password is required.'}
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
        error_messages={'required': 'Please confirm your password.'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")

        if len(password) > 20:
            raise ValidationError("Password cannot be longer than 20 characters.")

        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one number.")

        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")

        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character.")

        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already taken. Please choose a different one.")
        return email
