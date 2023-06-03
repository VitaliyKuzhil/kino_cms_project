from django import template
from user.models import *

register = template.Library()


@register.inclusion_tag('user/side_bar.html')
def render_menu_items():
    side_bar = [
        {'title': "Статистика", 'url': 'user:statistic', 'icon': 'fa-chart-line'},
        {'title': "Банера", 'url': 'user:banners', 'icon': 'fa-image'},
        {'title': "Фільми", 'url': 'cinema:list_films', 'icon': 'fa-film'},
        {'title': "Кінотеатри", 'url': 'cinema:list_cinemas', 'icon': 'fa-store'},
        {'title': "Новини", 'url': 'core:news', 'icon': 'fa-newspaper'},
        {'title': "Акції", 'url': 'core:shares', 'icon': 'fa-star'},
        {'title': "Сторінки", 'url': 'core:list_pages', 'icon': 'fa-layer-group'},
        {'title': "Користувачі", 'url': 'user:list_users', 'icon': 'fa-user'},
        {'title': "Розсилка", 'url': 'core:mailing', 'icon': 'fa-people-arrows'}
    ]
    return {'menu_items': side_bar}

