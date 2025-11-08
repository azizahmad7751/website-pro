from django import forms

class ContactForm(forms.Form):
    BUDGET_CHOICES = [
        ("Under $2,000", "Under $2,000"),
        ("$2,000 – $5,000", "$2,000 – $5,000"),
        ("$5,000 – $15,000", "$5,000 – $15,000"),
        ("$15,000+", "$15,000+"),
    ]
    name = forms.CharField(min_length=2, max_length=120)
    email = forms.EmailField()
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":6}), min_length=10)
