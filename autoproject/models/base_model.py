from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(
        'Creat',
        auto_now_add=True,
        help_text='Data en la l\'objecte va ser creat.',
    )

    modified = models.DateTimeField(
        'Actualitzat',
        auto_now=True,
        help_text='Data en la l\'objecte ha sigut actualitzat.',
    )

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
