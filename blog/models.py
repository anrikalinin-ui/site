from django.db import models


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    body = models.TextField('Текст')
    audio = models.FileField('Аудио', upload_to='blog/audio/', blank=True, null=True)
    video = models.FileField('Видео', upload_to='blog/video/', blank=True, null=True)
    video_url = models.URLField('Ссылка на видео (YouTube)', blank=True)
    created = models.DateTimeField('Дата', auto_now_add=True)
    published = models.BooleanField('Опубликован', default=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created']

    def __str__(self):
        return self.title
