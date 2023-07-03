from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'note', 'profile_photo']
        widgets = {'profile_photo': forms.FileInput(attrs={'accept': 'image/*'})}