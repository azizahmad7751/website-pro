from django.core.management.base import BaseCommand
from portfolio.models import Project
from careers.models import Job

class Command(BaseCommand):
    help = "Seed demo projects and jobs"

    def handle(self, *args, **options):
        if Project.objects.count() == 0:
            Project.objects.create(title="SaaS Dashboard", tag="Product", summary="Analytics dashboard with RBAC and charts.", slug="saas-dashboard")
            Project.objects.create(title="E-commerce Store", tag="Commerce", summary="High-conversion store with payments and search.", slug="ecommerce-store")
            Project.objects.create(title="Fintech Landing", tag="Marketing", summary="Marketing site with blog and CMS.", slug="fintech-landing")
        if Job.objects.count() == 0:
            Job.objects.create(title="Senior Full-Stack Engineer", type="Remote", location="Worldwide", description="React/Django, Postgres. 5+ yrs.", slug="senior-full-stack-engineer")
            Job.objects.create(title="Product Designer", type="Remote", location="Worldwide", description="Design systems, prototyping, handoff.", slug="product-designer")
        self.stdout.write(self.style.SUCCESS("Demo data seeded."))
