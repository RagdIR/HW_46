from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Note
from webapp.forms import NoteForm
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
            'form': NoteForm()
        })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = Note.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                text=form.cleaned_data['text'],
                todo_at=form.cleaned_data['todo_at'],
                status=form.cleaned_data['status'])
            return redirect('note_view', pk=note.pk)
        else:
            return render(request, 'note_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def note_update_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "GET":
        form = NoteForm(initial={
            'title': note.title,
            'description': note.description,
            'text': note.text,
            'todo_at': note.todo_at,
            'status': note.status,
        })
        return render(request, 'note_update.html', context={
            'form': form,
            'note': note
        })
    elif request.method == 'POST':
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note.title = form.cleaned_data['title']
            note.description = form.cleaned_data['description']
            note.text = form.cleaned_data['text']
            note.todo_at = form.cleaned_data['todo_at']
            note.status = form.cleaned_data['status']
            note.save()
            return redirect('note_view', pk=note.pk)
        else:
            return render(request, 'note_update.html', context={
                'note': note,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def note_delete_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        return render(request, 'note_delete.html', context={'note': note})
    elif request.method == 'POST':
        note.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

def delete(request):
    if request.method == 'POST':
        note = request.POST.getlist('check')
        Note.objects.filter(pk_in=note).delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])