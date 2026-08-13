from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteCreatForm
def index(request):
    notes = Note.objects.all().order_by('-data')
    return render(request, 'note/index.html', {'data':notes})

def note_visibel(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'note/index_note.html', {'noteid':note})

def index_create(request):
    if request.method == 'POST':
        form = NoteCreatForm(request.POST)
        if form.is_valid():
            form.save()


    form = NoteCreatForm()
    context = {
        'form':form
    }
    return render(request, 'note/index_create.html', context)