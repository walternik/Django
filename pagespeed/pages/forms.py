from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASSES = 'py-2 px-4 rounded-xl border w-96'
AUTH_CLASSES = 'w-full py-4 px-6 rounded-xl'

class PageForm(forms.Form):
    url1 = forms.CharField(
        label='URL 1',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'https://example-1.com',
                'class': INPUT_CLASSES
            }
        ),
    )
    url2 = forms.CharField(
        label='URL 2',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'https://example-2.com',
                'class': INPUT_CLASSES
            }
        ),
    )
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': AUTH_CLASSES
    }), max_length=100, required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': AUTH_CLASSES
    }), max_length=200, required=True)


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': AUTH_CLASSES
    }), max_length=100, required=True)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': AUTH_CLASSES
    }), max_length=100, required=False)

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': AUTH_CLASSES
    }), max_length=100, required=True)

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': AUTH_CLASSES
    }), max_length=100, required=True)