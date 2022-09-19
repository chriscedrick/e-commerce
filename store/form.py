
from django.contrib.auth.forms import UserCreationForm
from .models import Message, User, Comment
from django import forms
from django.forms import ModelForm

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ['fname', 'lname', 'email', 'subject', 'message']
        
class CommentSection(ModelForm):
    class Meta:
        model = Comment
        fields = ['product','fname','lname','comment_area']