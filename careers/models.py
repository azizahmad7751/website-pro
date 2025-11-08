from django.db import models
from django.utils.text import slugify

class Job(models.Model):
    JOB_TYPES = [("Remote","Remote"), ("Hybrid","Hybrid"), ("Onsite","Onsite")]
    title = models.CharField(max_length=160)
    type = models.CharField(max_length=20, choices=JOB_TYPES, default="Remote")
    location = models.CharField(max_length=160, default="Worldwide")
    slug = models.SlugField(unique=True, max_length=180)
    description = models.TextField()
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:180]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

def resume_upload_path(instance, filename):
    return f"applications/{instance.job.slug}/{filename}"

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    name = models.CharField(max_length=140)
    email = models.EmailField()
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to=resume_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} for {self.job.title}"
