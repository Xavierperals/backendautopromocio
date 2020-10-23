from django.db import models

from autoproject.models import BaseModel
from .project import Project


class ProjectImage(BaseModel):
    property = models.ForeignKey(Project, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='project_images')

    class Meta:
        verbose_name = 'Imatge de Projecte'
        verbose_name_plural = 'Imatges de Projecte'
