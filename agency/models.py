from django.db import models

from core import settings


class Topic(models.Model):
    name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="topics",
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="publishers"
    )

    def __str__(self):
        return self.title
