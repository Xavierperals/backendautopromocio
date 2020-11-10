from django.contrib import admin

from autoproject.models import FormContact


@admin.register(FormContact)
class FormContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'region', 'city', 'neighborhood',
        'house_price', 'size', 'rooms', 'comment',
        'name', 'phone_number', 'email',
        'wants_contact', 'creation_date'
    )

    readonly_fields = (
        'region', 'city', 'neighborhood',
        'house_price', 'initial_house_price', 'size', 'rooms',
        'comment', 'name', 'phone_number', 'email',
        'wants_contact', 'created', 'ip', 'browser',
        'browser_version', 'os', 'os_version',
        'device_family', 'device_brand', 'device_model',
        'raw_user_agent',
    )

    list_filter = (
        'region', 'city', 'size', 'wants_contact',
    )

    list_display_links = (
        'pk', 'name'
    )

    def creation_date(self, obj):
        return obj.created.strftime("%d %b %Y %H:%M")

    creation_date.admin_order_field = 'created'
    creation_date.short_description = 'Creat'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # actions = ['make_published']
    #
    # def make_published(self, request, queryset):
    #     self.message_user(request, 'test', messages.SUCCESS)
