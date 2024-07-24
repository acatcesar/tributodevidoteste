from meuapp.models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms

class FormMainPage(forms.Form):
    email = forms.EmailField(label=False)


class CreateAccountForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'endereco')