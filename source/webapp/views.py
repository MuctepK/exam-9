from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo
    extra_context = {"title": "Фото"}
    context_object_name = 'photos'

class PhotoCreateView(CreateView):
    template_name = 'create.html'
    model = Photo
    extra_context = {"title": "Фото"}


class PhotoUpdateView(UpdateView):
    template_name = 'update.html'
    model = Photo
    extra_context = {"title": "Фото"}


class PhotoDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Photo

