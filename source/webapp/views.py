from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')

def note_create_view(request):
    if request.method == 'GET':
        return render(request, 'note_create.html')
    elif request.method == 'POST':
        print(request.POST)
