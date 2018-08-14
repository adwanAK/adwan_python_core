from django.db import models

# Create your models here.

class Bookmark(models.Model):
    """docstring for Bookmark"""
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    bookmarks = models.Manager()

    def __str__(self):
        short_desc = f'{self.description[:20]}..' if len(self.description) > 20 else self.description
        return f'{self.title} | {self.url} | {short_desc}'
