from django.db import models

from autoproject.models import BaseModel


class FormContact(BaseModel):
    name = models.CharField(max_length=100)
