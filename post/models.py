from django.db import models
from django.conf import settings


class Post(models.Model):
    """Модель пост"""

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='posts/images/', verbose_name='Изображение', blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_editing = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Comment(models.Model):
    """Модель комментарии"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.CharField(max_length=250, verbose_name='комментарий')
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_editing = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'Комментарий #{self.pk} к посту {self.post}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
