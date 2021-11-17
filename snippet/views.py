from django.shortcuts import render, get_object_or_404
from snippet.models import Snippet
from .forms import SnippetForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def list_snippet(request):
    snippets = Snippet.objects.all().order_by("title")
    return render(request, "snippet/list_snippets.html", {"snippets": snippets})

@login_required
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


@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "GET":
        form = SnippetForm(instance=snippet)
    else:
        form = SnippetForm(data=request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect(to='list_snippet')
    return render(request, "snippet/edit_snippet.html", {"form": form, "snippet": snippet})


@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        snippet.delete()
        messages.success(request, "Snippet deleted.")
        return redirect(to="list_snippet")
    return render(request, "snippet/delete_snippet.html", {"snippet": snippet})

def search_snippet(request):
    query = request.GET.get("q")
    results = Snippet.objects.filter(
        Q(title__icontains=query)
    )
    print(query)
    return render(request, "snippet/list_snippets.html", {"snippets": results})

