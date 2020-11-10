from django.db import models

from autoproject.models import BaseModel
from autoproject.validators import validate_house_price_value
from autoproject.valueobjects import HomeSize, Rooms


class FormContact(BaseModel):
    # Location
    region = models.CharField(max_length=100, verbose_name='Comarca')
    city = models.CharField(max_length=100, verbose_name='Ciutat')
    neighborhood = models.CharField(max_length=100, null=True, blank=True, verbose_name='Barri')

    # House Price
    house_price = models.PositiveIntegerField(verbose_name='Preu', validators=[validate_house_price_value])

    # Size
    size = models.CharField(
        max_length=20, choices=[value[1] for value in HomeSize.choices()], verbose_name='Mida',
    )

    # Rooms
    rooms = models.CharField(
        max_length=30, choices=[value[1] for value in Rooms.choices()], verbose_name='Habitacions'
    )

    # Comment
    comment = models.CharField(max_length=250, verbose_name='Comentari')

    # User info
    name = models.CharField(max_length=100, verbose_name='Nom')
    phone_number = models.CharField(max_length=15, verbose_name='Telf')
    email = models.EmailField(max_length=250)

    # Wants more contact
    wants_contact = models.BooleanField(verbose_name='Contacte')

    # Metadata
    ip = models.GenericIPAddressField(verbose_name="IP", null=True)

    # User Agent Information
    browser = models.CharField(max_length=150, verbose_name='Navegador', null=True)
    browser_version = models.CharField(max_length=150, verbose_name='Versió de navegador', null=True)

    os = models.CharField(max_length=150, verbose_name='Sistema Operatiu', null=True)
    os_version = models.CharField(max_length=150, verbose_name='Versió de sistema operatiu', null=True)

    device_family = models.CharField(max_length=150, verbose_name='Familia de dispositiu', null=True)
    device_brand = models.CharField(max_length=150, verbose_name='Marca del dispositiu', null=True)
    device_model = models.CharField(max_length=150, verbose_name='Model del dispositiu', null=True)

    raw_user_agent = models.CharField(max_length=256, verbose_name='User Agent')

    class Meta:
        verbose_name = "Contacte Autoproject"
        verbose_name_plural = 'Contactes Autoproject'

    def initial_house_price(self) -> int:
        return int(self.house_price) * 0.2

    initial_house_price.short_description = 'En disposició (20%)'
