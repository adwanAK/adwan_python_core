from django.shortcuts import render
from rest_framework import generics
from . import serializer, models

# Create your views here.
class BookmarkList(generics.ListAPIView):
    """docstring for BookmarkList"""
    serializer_class = serializer.BookmarkSerializer
    queryset = models.Bookmark.bookmarks.all()
