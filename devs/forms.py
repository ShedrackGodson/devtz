from allauth.account.forms import SignupForm, LoginForm
from devs.models import Dev
from django import forms


class AddDevForm(SignupForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "name": "user-name", "class": "form-control"
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "name": "email", "class": "form-control"
    }))

    # class Meta:
    #     model = Dev
    #     fields = [
    #         "username", "email"
    #     ]

