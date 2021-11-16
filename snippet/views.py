from django.shortcuts import render
from snippet.models import Snippet
from .forms import SnippetForm
from django.shortcuts import render, redirect

# Create your views here.
def list_snippet(request):
    snippets = Snippet.objects.all().order_by("title")
    return render(request, "snippet/list_snippets.html", {"snippets": snippets})

def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/add_snippet.html", {"form": form})

# this should strip the pk and create a new one. 
# Don't know where this function should reside.
#this is NOT functional yet as well as copy_snippet.html
# def copy_snippet(request): 
#     if request.method == 'POST': 
#         snippet = Snippet.objects.get(pk=snippet_id)
#         snippet.pk = None
#         snippet.author = request.user
#         snippet.save()
    