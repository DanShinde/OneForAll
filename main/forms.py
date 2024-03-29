from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username','email', 'password1', 'password2']
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
            
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description"]
