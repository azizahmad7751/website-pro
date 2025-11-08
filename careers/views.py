from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Job
from .forms import ApplicationForm

def job_list(request):
    jobs = Job.objects.filter(is_open=True)
    return render(request, "careers/list.html", {"jobs": jobs})

def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug, is_open=True)
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)
            app.job = job
            app.save()
            messages.success(request, "Application submitted. We'll reach out soon.")
            return redirect("job_detail", slug=slug)
    else:
        form = ApplicationForm()
    return render(request, "careers/detail.html", {"job": job, "form": form})
