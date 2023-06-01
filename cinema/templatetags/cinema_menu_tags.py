from django import template
from cinema.models import *

register = template.Library()


@register.inclusion_tag('cinema/nav_bar.html', name='nav_bar')
def cinema_menu():
    nav_bar = [{'title': "Афіша"},
               {'title': "Розклад"},
               {'title': "Скоро"},
               {'title': "Кінотеатри"},
               {'title': "Акції"},
               {'title': "Про кінотеатр",
                'list': {'Новини': "home", 'Реклама': "addcinema", 'Кафе': "home", 'Мобільний додаток': 'cdc',
                         'Контакти': 'ece'}}]
    return {'nav_bar': nav_bar}
