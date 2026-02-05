from django.contrib import admin
from .models import Technology, Project

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'get_technologies')
    list_filter = ('status', 'technology')
    search_fields = ('name', 'description')

    def get_technologies(self, obj):
        return ", ".join([t.name for t in obj.technology.all()])
    get_technologies.short_description = "Technologies"