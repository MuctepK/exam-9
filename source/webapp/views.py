from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from webapp.forms import PhotoForm, CommentForm
from webapp.models import Photo


@method_decorator(ensure_csrf_cookie, name='dispatch')
class PhotoListView(ListView):
    template_name = 'index.html'
    model = Photo
    extra_context = {"title": "Фото"}
    context_object_name = 'photos'

    def get_queryset(self):
        return Photo.objects.all().order_by('-created_at')


@method_decorator(ensure_csrf_cookie, name='dispatch')
class PhotoDetailView(DetailView):
    template_name = 'photo.html'
    model = Photo

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['form'] = CommentForm
        return context


class PhotoCreateView(LoginRequiredMixin, CreateView):
    form_class = PhotoForm
    template_name = 'create.html'
    model = Photo
    extra_context = {"title": "Фото"}
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:detail_photo", kwargs={"pk": self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = PhotoForm
    template_name = 'update.html'
    model = Photo
    extra_context = {"title": "Фото"}
    permission_required = 'webapp.change_photo'

    def get_success_url(self):
        return reverse("webapp:detail_photo", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class PhotoDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

