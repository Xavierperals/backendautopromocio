from django.contrib import admin

from autoproject.models import FormContact


@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'region', 'city', 'neighborhood',
        'size', 'house_price', 'comment',
        'name', 'phone_number', 'email',
        'wants_contact', 'created'
    )

    readonly_fields = (
        'region', 'city', 'neighborhood',
        'size', 'house_price', 'comment',
        'name', 'phone_number', 'email',
        'wants_contact', 'created'
    )

    list_filter = (
        'region', 'city', 'size', 'wants_contact',
    )

    list_display_links = (
        'pk', 'name'
    )
