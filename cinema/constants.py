from django.db import models


class StatusMovieChoices(models.TextChoices):
    NEW = ('new', 'Новинка')
    SOON = ('soon', 'Скоро в прокаті')
    OLD = ('old', 'Старий фільм')
