from .models import Note
from django.forms import ModelForm

class NoteCreatForm(ModelForm):
    class Meta:
        model = Note
        fields  = ['name', 'brief', 'text']