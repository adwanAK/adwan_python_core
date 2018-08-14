from django.db import models

# Create your models here.
class Note(models.Model):
    """docstring for Note"""
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # change the manager name:
    # https://docs.djangoproject.com/en/1.10/topics/db/managers/#django.db.models.Manager
    notes = models.Manager()

    def __str__(self):
        return f'{self.title} {self.body}'
