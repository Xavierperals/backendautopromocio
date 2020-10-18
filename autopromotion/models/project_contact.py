from autoproject.models import BaseModel
from django.db import models

# from autopromotion.models import Project


class ProjectContact(BaseModel):

    # property = models.ForeignKey(Project)

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    comment = models.TextField()

    class Meta:
        verbose_name = 'Contacte de Projecte'
        verbose_name_plural = 'Contactes de Projecte'
