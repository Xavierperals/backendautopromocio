from django.db import models

from autoproject.models import BaseModel
from autoproject.valueobjects.home_size import HomeSize


class FormContact(BaseModel):

    # Location
    region = models.CharField(max_length=100, verbose_name='Comarca')
    city = models.CharField(max_length=100, verbose_name='Ciutat')
    neighborhood = models.CharField(max_length=100, null=True, blank=True, verbose_name='Barri')

    # Size
    size = models.CharField(
        max_length=20, choices=[value[1] for value in HomeSize.choices()], verbose_name='Mida',
    )

    # House Price
    house_price = models.IntegerField(verbose_name='Preu')

    # Comment
    comment = models.CharField(max_length=250, verbose_name='Comentari')

    # User info
    name = models.CharField(max_length=100, verbose_name='Nom')
    phone_number = models.CharField(max_length=15, verbose_name='Telf')
    email = models.EmailField(max_length=250)

    # Wants more contact
    wants_contact = models.BooleanField(verbose_name='Vol ser contactat?')

    class Meta:
        verbose_name = "Contacte Autoproject"
        verbose_name_plural = 'Contactes Autoproject'

    def initial_house_price(self) -> float:
        return self.house_price * 0.20

    initial_house_price.short_description = 'En disposició (20%)'
