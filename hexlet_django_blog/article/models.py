from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
