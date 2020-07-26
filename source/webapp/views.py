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
        status = request.POST.get('status')
        note = Note.objects.create(title=title, text=text, status=status)
        context = {'note': note}
        return render(request, 'note_view.html', context)

def note_view(request):
    note_id = request.GET.get('pk')
    note = Note.objects.get(pk=note_id)
    context = {'note': note}
    return render(request, 'note_view.html', context)
