from django.contrib import admin
from autoproject.models import FormContact


@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
