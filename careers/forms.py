from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["name","email","cover_letter","resume"]
        widgets = {
            "cover_letter": forms.Textarea(attrs={"rows":6})
        }
