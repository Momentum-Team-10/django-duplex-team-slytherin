from django.shortcuts import render
from snippet.models import Snippet
from .forms import SnippetForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def list_snippet(request):
    snippet = Snippet.objects.all().order_by("title")
    return render(request, "snippet/list_snippets.html", {"snippet": snippet})

def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/add_snippet.html", {"form": form})

def edit_snippet(request, pk):
    snippet = Snippet.objects.get(id=pk)
    if request.method == 'POST':
        snippet.title = request.POST['title']
        snippet.author = request.POST['author']
        snippet.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'snippet/edit_snippet.html', {'snippet': snippet})