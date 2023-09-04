from django.urls import path, include
from .views import *

urlpatterns = [
    path('news/', news_view, name='news'),
    path('cafe_bar/', cafe_bar_view, name='cafe_bar'),
    path('vip_hall/', vip_hall_view, name='vip_hall'),
    path('children_room/', children_room_view, name='children_room'),
    path('advertise/', advertise_view, name='advertise'),
    path('mobile_app/', mobile_app, name='mobile_app'),
    path('contacts/', contacts_view, name='contacts'),
    path('shares/', shares_view, name='shares'),
    path('list_pages/', list_pages, name='list_pages'),
    path('mailing/', mailing_view, name='mailing'),
]
