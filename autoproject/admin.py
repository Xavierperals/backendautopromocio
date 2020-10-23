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
        'region', 'city', 'neighborhood', 'size',
        'house_price', 'initial_house_price', 'comment',
        'name', 'phone_number', 'email', 'wants_contact', 'created',
    )

    list_filter = (
        'region', 'city', 'size', 'wants_contact',
    )

    list_display_links = (
        'pk', 'name'
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # actions = ['make_published']
    #
    # def make_published(self, request, queryset):
    #     self.message_user(request, 'test', messages.SUCCESS)
