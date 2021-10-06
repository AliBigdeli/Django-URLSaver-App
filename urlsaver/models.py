from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=2000)
    descriptions = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

    def __str__(self):

        return self.url
