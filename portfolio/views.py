from django.shortcuts import render, get_object_or_404
from .models import Project

def portfolio_list(request):
    projects = Project.objects.all()
    return render(request, "portfolio/list.html", {"projects": projects})

def portfolio_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/detail.html", {"project": project})
