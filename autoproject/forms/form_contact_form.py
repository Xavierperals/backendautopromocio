from django import forms

from autoproject.models import FormContact


class FormContactForm(forms.ModelForm):
    class Meta:
        model = FormContact
        fields = [
            'region',
            'city',
            'neighborhood',
            'house_price',
            'size',
            'rooms',
            'comment',
            'name',
            'phone_number',
            'email',
            'wants_contact',
        ]
