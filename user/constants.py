from django.db import models
from django.conf.locale import LANG_INFO


class GenderChoices(models.TextChoices):
    MALE = ('male', 'Чоловіча')
    FEMALE = ('female', 'Жіноча')
    OTHER = ('other', 'Інша')


LANGUAGE_CHOICES = [
    (code, LANG_INFO.get(code)['name'] if 'name' in LANG_INFO.get(code) else code)
    for code in LANG_INFO
]
