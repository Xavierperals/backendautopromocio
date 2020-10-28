from django.db import models

from autoproject.models import BaseModel
from .project import Project


class ProjectContact(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)

    comment = models.TextField()

    class Meta:
        verbose_name = 'Contacte de Projecte'
        verbose_name_plural = 'Contactes de Projecte'
