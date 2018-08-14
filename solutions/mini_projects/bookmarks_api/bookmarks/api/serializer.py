from rest_framework import serializers
from . import models

class BookmarkSerializer(serializers.ModelSerializer):
    """docstring for BookmarkSerializer"""
    class Meta:
        model = models.Bookmark
        # leaving out 'created_at' to not show it in the output
        fields = ('title', 'url', 'description')
