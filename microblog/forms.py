from django import forms
from microblog.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['blogs','id']
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude=['id']

class LoginForm(forms.Form):
    name = forms.CharField(max_length=64)
