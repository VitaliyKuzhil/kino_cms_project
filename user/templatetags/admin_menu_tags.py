from django import template
from user.models import *

register = template.Library()


@register.inclusion_tag('user/side_bar.html')
def render_menu_items():
    side_bar = [
        {'title': "Statistic", 'url': 'user:statistic_admin', 'icon': 'fa-chart-line'},
        {'title': "Banners", 'url': 'user:banners_admin', 'icon': 'fa-image'},
        {'title': "Movies", 'url': 'user:list_films_admin', 'icon': 'fa-film'},
        {'title': "Cinemas", 'url': 'user:list_cinemas_admin', 'icon': 'fa-store'},
        {'title': "News", 'url': 'user:news_admin', 'icon': 'fa-newspaper'},
        {'title': "Shares", 'url': 'user:shares_admin', 'icon': 'fa-star'},
        {'title': "Pages", 'url': 'user:list_pages_admin', 'icon': 'fa-layer-group'},
        {'title': "Users", 'url': 'user:list_users_admin', 'icon': 'fa-user'},
        {'title': "Mailing", 'url': 'user:mailing_admin', 'icon': 'fa-people-arrows'}
    ]
    return {'menu_items': side_bar}

