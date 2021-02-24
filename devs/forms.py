from allauth.account.forms import SignupForm, LoginForm
from ckeditor.widgets import CKEditorWidget
from devs.models import Dev, OtherExperience
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

class AddOtherExperienceForm(forms.ModelForm):
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control autofocus", "placeholder": "Enter subject..."
    }))

    description = forms.CharField(required=True, widget=CKEditorWidget(attrs={
        "class": "form-control autofocus", "placeholder": "Enter description...",
    }))

    def save(self, commit, dev):
        experience = super(AddOtherExperienceForm, self).save(commit=False)
        experience.dev = dev
        experience.save()
        return experience

    class Meta:
        model = OtherExperience
        fields = ["subject", "description"]