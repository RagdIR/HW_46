from django.shortcuts import render
from webapp.models import Note


def index_view(request):
    data = Note.objects.all()
    return render(request, 'index.html', context={'notes': data})

def note_create_view(request):
    if request.method == 'GET':
        return render(request, 'note_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        note = Note.objects.create(title=title, text=text)
        context = {'note': note}
        return render(request, 'note_view.html', context)

