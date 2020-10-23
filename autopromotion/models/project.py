from typing import List

from django.db import models

from autoproject.models import BaseModel


class Project(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Títol')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítol')
    description = models.TextField(default='', verbose_name='Descripció')

    location = models.CharField(
        max_length=100,
        verbose_name='Localització'
    )
    maps_location = models.CharField(
        max_length=256,
        verbose_name='Localització Google Maps',
    )

    # pictures = models.FileField()  # TODO relationship
    amenties = models.CharField(
        max_length=500,
        verbose_name='Caracteristiques',
        help_text='Escriu, separat per comes, les caracteristiques del projecte.',
        default='',
    )

    properties_number_total = models.IntegerField(
        default=0,
        verbose_name='Propietats totals',
        help_text='Nombre de propietats totals del projecte',
    )
    properties_number_rest = models.IntegerField(
        default=0,
        verbose_name='Propietats restants',
        help_text='Nombre de propietats restants que encara queden en el projecte',
    )

    min_price = models.IntegerField(default=100000, verbose_name='Preu mínim')

    status = models.CharField(
        max_length=20,
        choices=(
            ('active', 'Activa'),
            ('finished', 'Finalitzat'),
        ),
        verbose_name='Estat',
    )

    home_page = models.BooleanField(
        default=False,
        verbose_name='Pàgina principal?',
        help_text='Ha d\'aparèixer a la pàgina principal?',
    )

    class Meta:
        verbose_name = 'Projecte'
        verbose_name_plural = 'Projectes'

    def splitted_amenties(self) -> List[str]:

        amenties: str = self.amenties

        if amenties == '':
            return []

        return [amenty.strip() for amenty in amenties.split(',')]
