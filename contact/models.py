from django.db import models


class Message(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    text = models.TextField('Сообщение')
    created = models.DateTimeField('Дата', auto_now_add=True)
    handled = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created']

    def __str__(self):
        return f'{self.name} ({self.email})'
