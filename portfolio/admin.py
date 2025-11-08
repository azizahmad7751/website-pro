from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","tag","created_at")
    search_fields = ("title","tag","summary")
    prepopulated_fields = {"slug": ("title",)}
