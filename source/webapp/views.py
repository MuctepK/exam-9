from django.shortcuts import render
from django.views.generic import ListView, CreateView

from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo

class PhotoCreateView(CreateView):
    template_name = 'create.html'

