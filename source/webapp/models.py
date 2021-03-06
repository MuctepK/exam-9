from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    img = models.ImageField(verbose_name='Фотография', upload_to='images')
    signature = models.CharField(verbose_name='Подпись', max_length=256)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    likes = models.PositiveIntegerField(verbose_name='Количество лайков', blank=True, default=0)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='photos')

    def __str__(self):
        return "Фото от {}".format(self.author.username)

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.likes -= 1
        self.save()


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return "Комментарий от {}".format(self.author.username)


class LikeSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photos')

    def save(self, *args, **kwargs):
        super().save()
        self.photo.like()

    def delete(self, using=None, keep_parents=False):
        self.photo.dislike()
        super().delete()

