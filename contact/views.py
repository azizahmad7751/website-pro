from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Inquiry

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Inquiry.objects.create(**data)
            subject = f"New Inquiry from {data['name']}"
            body = f"Name: {data['name']}\nEmail: {data['email']}\nBudget: {data.get('budget','')}\n\n{data['message']}"
            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_TO_EMAIL])
            messages.success(request, "Thanks! We'll be in touch soon.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
