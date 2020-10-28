from django import forms

from autopromotion.models import ProjectContact


class ProjectContactForm(forms.ModelForm):
    class Meta:
        model = ProjectContact
        fields = [
            'name',
            'phone',
            'email',
            'comment',
        ]
