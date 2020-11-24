from django.db import models

from autoproject.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Contacte'
        verbose_name_plural = 'Contactes'
