from django import forms

from autoproject.models import FormContact


class FormContactForm(forms.ModelForm):
    class Meta:
        model = FormContact
        fields = [
            'region',
            'city',
            'neighborhood',
            'size',
            'house_price',
            'comment',
            'name',
            'phone_number',
            'email',
            'wants_contact',
        ]
