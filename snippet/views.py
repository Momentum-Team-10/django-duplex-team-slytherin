from django.shortcuts import render, get_object_or_404
import snippet
from snippet.models import Snippet
from .forms import SnippetForm
from django.shortcuts import render, redirect



def list_snippet(request):
    snippets = Snippet.objects.all().order_by("title")
    return render(request, "snippet/list_snippets.html", {"snippets": snippets})

def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/add_snippet.html", {"form": form})

def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    # breakpoint()
    if request.method == "GET":
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/edit_snippet.html", {"form": form, "snippet": snippet})
    
    
    
    