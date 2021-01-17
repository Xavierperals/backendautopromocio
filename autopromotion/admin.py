from django.contrib import admin

from autopromotion.models import Project, ProjectContact, ProjectImage, Contact


class ProjectImageAdmin(admin.TabularInline):
    model = ProjectImage


@admin.register(ProjectContact)
class ProjectContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'project', 'phone', 'email',
    )

    readonly_fields = (
        'pk', 'project', 'name', 'phone', 'email', 'comment',
    )

    list_filter = (
        'project__title', 'phone', 'email',
    )

    list_display_links = (
        'pk', 'name'
    )

    def has_add_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'subtitle', 'properties_number_total',
        'properties_number_rest', 'min_price', 'status', 'home_page', 'created',
        'modified',
    )

    list_filter = (
        'status', 'home_page',
    )

    list_display_links = (
        'pk', 'title',
    )

    inlines = (
        ProjectImageAdmin,
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'phone', 'email',
    )

    readonly_fields = (
        'pk', 'name', 'phone', 'email', 'comment',
    )

    list_filter = (
        'phone', 'email',
    )

    list_display_links = (
        'pk', 'name'
    )

    def has_add_permission(self, request, obj=None) -> bool:
        return False

    def has_change_permission(self, request, obj=None) -> bool:
        return False
