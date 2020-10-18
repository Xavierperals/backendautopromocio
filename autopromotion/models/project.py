from autoproject.models import BaseModel
from django.db import models


class Project(BaseModel):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()

    location = models.CharField(max_length=100)
    maps_location = models.CharField(max_length=256)

    # pictures = models.FileField()  # TODO relationship
    # amenities = models.CharField()  # TODO relationship

    properties_number_total = models.IntegerField()
    properties_number_rest = models.IntegerField()

    min_price = models.IntegerField()

    status = models.CharField(max_length=20, choices=(
        ('active', 'Activa'),
        ('finished', 'Finalitzat'),
    ))

    home_page = models.BooleanField(default=False, verbose_name='Ha d\'aparèixer a la pàgina principal?')

    class Meta:
        verbose_name = 'Projecte'
        verbose_name_plural = 'Projectes'
