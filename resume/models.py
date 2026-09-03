from django.db import models


class Metric(models.Model):
    value = models.CharField('Значение', max_length=50)
    label = models.CharField('Подпись', max_length=150)
    order = models.PositiveSmallIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Метрика'
        verbose_name_plural = 'Метрики'
        ordering = ['order']

    def __str__(self):
        return f'{self.value} — {self.label}'


class Profile(models.Model):
    full_name = models.CharField('ФИО', max_length=100)
    title = models.CharField('Должность', max_length=100)
    location = models.CharField('Город', max_length=100, blank=True)
    bio = models.TextField('О себе', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField('Телефон', max_length=30, blank=True)
    photo = models.ImageField('Фото', upload_to='profile/', blank=True, null=True)
    show_photo = models.BooleanField('Показывать фото', default=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

    def __str__(self):
        return self.full_name


class Language(models.Model):
    name = models.CharField('Язык', max_length=100)
    level = models.CharField('Уровень', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['id']

    def __str__(self):
        return self.name


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
    summary = models.TextField('Краткое описание', blank=True)
    duties = models.TextField('Функционал (по строке на пункт)', blank=True)
    results = models.TextField('Ключевые результаты (по строке на пункт)', blank=True)

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.position} — {self.company}'

    def duties_list(self):
        return [l for l in self.duties.splitlines() if l.strip()]

    def results_list(self):
        return [l for l in self.results.splitlines() if l.strip()]


class Education(models.Model):
    KIND_HIGHER = 'higher'
    KIND_COURSE = 'course'
    KIND_CHOICES = [
        (KIND_HIGHER, 'Высшее'),
        (KIND_COURSE, 'Курсы'),
    ]

    kind = models.CharField('Тип', max_length=20, choices=KIND_CHOICES, default=KIND_HIGHER)
    year = models.CharField('Год', max_length=20)
    place = models.CharField('Место', max_length=200)
    program = models.CharField('Специальность/программа', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = ['-year']

    def __str__(self):
        return f'{self.year} — {self.place}'


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
