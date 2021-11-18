"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from snippet import views as snippet_views

urlpatterns = [
    path("", snippet_views.list_snippet, name="list_snippet"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
    path('snippet/add_snippet/', snippet_views.add_snippet, name='add_snippet'),
    path('snippet/<int:pk>/edit', snippet_views.edit_snippet, name='edit_snippet'),
    path('snippet/<int:pk>/delete', snippet_views.delete_snippet, name='delete_snippet'),
    path('search', snippet_views.search_snippet, name='search_snippet'),
    path("snippets/<int:pk>", snippet_views.show_snippet, name="show_snippet"),    
]
