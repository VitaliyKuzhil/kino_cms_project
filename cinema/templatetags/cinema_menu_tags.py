from django import template
from cinema.models import *

register = template.Library()


@register.inclusion_tag('cinema/nav_bar.html', name='nav_bar')
def cinema_menu():
    nav_bar = [{'title': "Головна", 'url': 'cinema:home_page'},
               {'title': "Афіша", 'url': 'cinema:list_films'},
               {'title': "Розклад", 'url': 'cinema:sessions'},
               {'title': "Скоро", 'url': 'cinema:list_films'},
               {'title': "Кінотеатри", 'url': 'cinema:list_cinemas'},
               {'title': "Акції", 'url': 'core:shares'},
               {'title': "Про кінотеатр",
                'list': ({'title': 'Новини', 'url': 'cinema:list_films'},
                         {'title': 'Реклама', 'url': 'cinema:list_films'},
                         {'title': 'Кафе', 'url': 'cinema:list_films'},
                         {'title': 'Мобільний додаток', 'url': 'cinema:list_films'},
                         {'title': 'Контакти', 'url': 'cinema:list_films'})
                }]
    return {'nav_bar': nav_bar}
