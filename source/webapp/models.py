from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    img = models.ImageField(verbose_name='Фотография', upload_to='images')
    signature = models.CharField(verbose_name='Подпись', max_length=256)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    likes = models.PositiveIntegerField(verbose_name='Количество лайков', blank=True, default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='photos')


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
