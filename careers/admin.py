from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title","type","location","is_open","created_at")
    list_filter = ("type","is_open")
    search_fields = ("title","location","description")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job","name","email","created_at")
    search_fields = ("name","email","cover_letter")
    list_filter = ("job",)
