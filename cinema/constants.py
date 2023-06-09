from django.db import models


class TypeMovieChoices(models.TextChoices):
    D2 = ('2d', '2D')
    D3 = ('3d', '3D')
    IMAX = ('imax', 'IMAX')


class StatusMovieChoices(models.TextChoices):
    NEW = ('new', 'Новинка')
    SOON = ('soon', 'Скоро в прокаті')
    OLD = ('old', 'Старий фільм')
