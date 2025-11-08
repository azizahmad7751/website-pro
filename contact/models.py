from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    budget = models.CharField(max_length=60, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
