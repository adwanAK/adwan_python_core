from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from api.models import Note


class NoteResource(ModelResource):
    """docstring for NoteResource"""
    class Meta:
        """docstring for Meta"""
        queryset = Note.notes.all()
        resource_name = 'note'
        # add authorization to allow the CUD of CRUD
        authorization = Authorization()
        # limiting which fields are visible in the JSON response
        fields = ['title', 'body']
