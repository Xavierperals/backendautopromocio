from django.contrib import admin

from autopromotion.models import Project, ProjectContact, ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'title', 'subtitle', 'location', 'properties_number_total',
        'properties_number_rest', 'min_price', 'status', 'home_page', 'created',
        'modified',
    )

    list_filter = (
        'status', 'home_page',
    )

    list_display_links = (
        'pk', 'title',
    )


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'name', 'project', 'created',
    )

    list_filter = (
        'project',
    )

    list_display_links = (
        'pk', 'name',
    )


@admin.register(ProjectContact)
class ProjectContactAdmin(admin.ModelAdmin):
    pass
