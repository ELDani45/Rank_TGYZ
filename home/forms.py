from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class SignIn(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input'
    }))


class Registrate(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "input"
    }))

    class Meta:
        model = User
        fields = ("name", "password",)


#  Widget = Representacin en el html
#  forms.Charfield = representacio en la bases de datos
