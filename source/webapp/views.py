from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Note, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    data = Note.objects.all()
    return render(request, 'index.html', context={'notes': data})


def note_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {'note': note}
    return render(request, 'note_view.html', context)


def note_create_view(request):
    if request.method == 'GET':
        return render(request, 'note_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('content')
        status = request.POST.get('status')
        note = Note.objects.create(title=title, text=text, status=status)
        return redirect('note_view', pk=note.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


