from django.db import models
from django.conf.locale import LANG_INFO
from geonamescache import GeonamesCache


class GenderChoices(models.TextChoices):
    MALE = ('male', 'Male')
    FEMALE = ('female', 'Female')
    OTHER = ('other', 'Other')


LANGUAGE_CHOICES = [
    (code, LANG_INFO.get(code)['name'] if 'name' in LANG_INFO.get(code) else code)
    for code in LANG_INFO
]

LANGUAGE_CHOICES.sort(key=lambda x: x[1])


def get_city_choices():
    gc = GeonamesCache()
    cities = gc.get_cities()
    city_choices = sorted([(city['name'].lower(), city['name']) for city in cities.values()])
    return city_choices


CITY_CHOICES = get_city_choices()
