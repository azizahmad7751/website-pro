from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=140)
    tag = models.CharField(max_length=60, blank=True)
    summary = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=160)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:160]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
