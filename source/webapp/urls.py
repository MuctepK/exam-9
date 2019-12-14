from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from webapp.views import PhotoListView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', PhotoListView.as_view(), name='index'),
    path('create/', PhotoCreateView.as_view(), name='create_photo'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='update_photo'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete_photo')
]
app_name = 'webapp'