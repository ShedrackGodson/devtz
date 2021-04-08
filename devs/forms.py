from allauth.account.forms import SignupForm, LoginForm
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import Textarea
from devs.models import Dev, DevCertificates, OtherExperience
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


class AddCertificateForm(forms.ModelForm):
    certificate_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control autofocus", "placeholder": "Enter name..."
    }))

    certificate_id = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control autofocus", "placeholder": "Enter ID..."
    }))

    provider = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control autofocus", "placeholder": "Enter provider..."
    }))

    description = forms.CharField(required=True, widget=Textarea(attrs={
        "class": "form-control autofocus", "cols": 0, "rows": 2, "placeholder": "Enter description...",
    }))

    issue_date = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control", "type": "date"
    }))

    expiration = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "type": "date"
    }))

    certificate_url = forms.URLField(required=False, widget=forms.URLInput(attrs={
        "class": "form-control"
    }))

    def save(self, commit, dev):
        certificate = super(AddCertificateForm, self).save(commit=False)
        certificate.dev = dev
        certificate.save()
        return certificate

    class Meta:
        model = DevCertificates
        fields = [
            "certificate_name", "provider", "description", "issue_date",
            "expiration", "certificate_id", "certificate_url"
        ]

