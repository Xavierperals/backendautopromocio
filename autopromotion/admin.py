from django.contrib import admin

from autopromotion.models import Project, ProjectContact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectContact)
class ProjectContactAdmin(admin.ModelAdmin):
    pass
