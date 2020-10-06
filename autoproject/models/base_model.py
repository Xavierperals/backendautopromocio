from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(
        'created_at', auto_now_add=True, help_text='datetime the object was created'
    )

    modified = models.DateTimeField(
        'modified_at', auto_now=True, help_text='datetime the object was modified'
    )

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
