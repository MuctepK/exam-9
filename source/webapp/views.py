from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo
    extra_context = {"title": "Фото"}
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.all().order_by('-created_at')


class PhotoCreateView(CreateView):
    form_class = PhotoForm
    template_name = 'create.html'
    model = Photo
    extra_context = {"title": "Фото"}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(UpdateView):
    template_name = 'update.html'
    model = Photo
    extra_context = {"title": "Фото"}


class PhotoDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Photo

