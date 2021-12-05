from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Post, Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'file',)


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar',)