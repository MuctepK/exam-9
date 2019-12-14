from django.shortcuts import render
from django.views.generic import ListView

from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo

