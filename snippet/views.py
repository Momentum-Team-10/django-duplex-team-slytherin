from django.shortcuts import render
from snippet.models import Snippet
from .forms import SnippetForm
from django.shortcuts import render, redirect

# Create your views here.
def list_snippet(request):
    snippet = Snippet.objects.all().order_by("title")
    return render(request, "snippet/list_snippet.html", {"snippet": snippet})

def add_snippet(request):
    if request.method == 'GET':
        form = SnippetForm()
    else:
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/add_snippet.html", {"form": form})