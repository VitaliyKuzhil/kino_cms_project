from django import template
from core.models import *

register = template.Library()


@register.inclusion_tag('cinema/nav_bar.html', name='nav_bar')
def cinema_menu():
    home = HomePage.objects.filter(status_page=True).first()
    about_cinema = AboutCinemaPage.objects.filter(status_page=True).first()
    cafe_bar = CafeBarPage.objects.filter(status_page=True).first()
    vip_hall = VipHallPage.objects.filter(status_page=True).first()
    advertise = AdvertisePage.objects.filter(status_page=True).first()
    children_room = ChildrenRoomPage.objects.filter(status_page=True).first()
    contacts = Pages.objects.filter(status_page=True).get(name_page='Contacts page')

    nav_bar = [{'title': home.name_page, 'url': 'cinema:home_page'} if home else None,
               {'title': "Poster", 'url': 'cinema:list_films_all'},
               {'title': "Sessions", 'url': 'cinema:sessions'},
               {'title': "Soon", 'url': 'cinema:list_films_soon'},
               {'title': "Cinemas", 'url': 'cinema:list_cinemas'},
               {'title': "Shares", 'url': 'cinema:shares_user'},
               {'title': about_cinema.name_page, 'url': 'cinema:about_cinema_user',
                'list': [{'title': 'News', 'url': 'cinema:news_user'},
                         {'title': cafe_bar.name_page, 'url': 'cinema:cafe_bar_user'} if cafe_bar else None,
                         {'title': vip_hall.name_page, 'url': 'cinema:vip_hall_user'} if vip_hall else None,
                         {'title': children_room.name_page, 'url': 'cinema:children_room_user'} if children_room else None,
                         {'title': advertise.name_page, 'url': 'cinema:advertise_user'} if advertise else None,
                         {'title': 'Mobie app', 'url': 'cinema:mobile_app_user'},
                         {'title': contacts.name_page, 'url': 'cinema:contacts_user'} if contacts else None,
                         *[
                             {'title': page.name_page, 'url': 'cinema:custom_page'}
                             for page in CustomPage.objects.filter(status_page=True)
                         ]
                         ]
                } if about_cinema else None]
    return {'nav_bar': nav_bar}
