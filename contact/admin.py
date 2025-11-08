from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("name","email","budget","created_at")
    search_fields = ("name","email","message")
    list_filter = ("budget",)
