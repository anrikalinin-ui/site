from django.db import models


class Profile(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    title = models.CharField('Должность', max_length=100)
    bio = models.TextField('О себе', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    photo = models.ImageField('Фото', upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.full_name


class Skill(models.Model):
    name = models.CharField('Название', max_length=100)
    level = models.PositiveSmallIntegerField('Уровень (1-10)', default=5)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField('Компания', max_length=200)
    position = models.CharField('Должность', max_length=200)
    start_date = models.DateField('Начало')
    end_date = models.DateField('Окончание', blank=True, null=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.position} — {self.company}'


class Project(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    url = models.URLField('Ссылка', blank=True)
    image = models.ImageField('Изображение', upload_to='projects/', blank=True, null=True)
    technologies = models.CharField('Технологии', max_length=300, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created']

    def __str__(self):
        return self.title
