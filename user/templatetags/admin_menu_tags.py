from django import template
from user.models import *

register = template.Library()


@register.inclusion_tag('user/side_bar.html', name='side_bar')
def cinema_menu():
    side_bar = [{'title': "Статистика", 'url': 'home', 'icon': 'fas fa-chart-pie', 'list': {}},
            {'title': "Банера", 'url': 'baners', 'icon': 'far fa-image', 'list': {}},
            {'title': "Фільми", 'url': 'add_film', 'icon': 'fa-sharp fa-solid fa-film',
             'list': {'Список фільмів': "list_films", 'Добавити фільм': "add_film"}},
            {'title': "Кінотеатри", 'url': 'add_cinema', 'icon': 'fa-solid fa-user',
             'list': {'Список кінотеатрів': "list_cinemas", 'Добавити кінотеатр': "add_cinema", 'Добавити зал': "add_hall"}},
            {'title': "Новини", 'url': 'news', 'icon': 'fa-solid fa-newspaper', 'list': {'Добавити новину': "add_news"}},
            {'title': "Акції", 'url': 'shares', 'icon': 'fa-regular fa-star', 'list': {'Добавити акцію': "add_share"}},
            {'title': "Сторінки", 'url': 'pages', 'icon': 'fa-solid fa-table-list',
             'list': {'Головна сторінка': "home", "Про кінотеатр": "home", "Кафе-Бар": "cafe_bar", "Vip-зал": "vip_hall",
                      "Реклама": "adv", "Дитяча кімната": "children_room", "Контакти": "contacts"}},
            {'title': "Користувачі", 'url': 'list_users', 'icon': 'fa-solid fa-user', 'list': {}},
            {'title': "Розсилка", 'url': 'mailing', 'icon': 'fa-solid fa-envelopes-bulk', 'list': {}}
            ]
    return {'side_bar': side_bar}

