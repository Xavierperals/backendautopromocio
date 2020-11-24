from django import forms

from autopromotion.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'phone',
            'email',
            'comment',
        ]
