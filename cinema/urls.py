from django.urls import path, include

from .views import *
from user.views import login_view, register_view, logout_view, profile_view
from core.views import shares_view, detail_shares, about_cinema_view, news_view, detail_news, cafe_bar_view, vip_hall_view,\
    children_room_view, advertise_view, mobile_app, contacts_view, custom_page_view

urlpatterns = [
    path('', home_page, name='home_page'),
    path('profile/', profile_view, name='profile_user'),
    path('sessions/', sessions, name='sessions'),
    path('list_films_all/', list_films_all, name='list_films_all'),
    path('list_films_soon/', list_films_soon, name='list_films_soon'),
    path('list_films_all/<int:pk>/', detail_film, name='detail_film_all'),
    path('list_films_soon/<int:pk>/', detail_film, name='detail_film_soon'),
    path('list_cinemas/', list_cinemas, name='list_cinemas'),
    path('shares/', shares_view, name='shares_user'),
    path('shares/<int:pk>', detail_shares, name='detail_shares'),
    path('about_cinema/', about_cinema_view, name='about_cinema_user'),
    path('news/', news_view, name='news_user'),
    path('news/<int:pk>', detail_news, name='detail_news'),
    path('cafe_bar/', cafe_bar_view, name='cafe_bar_user'),
    path('vip_hall/', vip_hall_view, name='vip_hall_user'),
    path('children_room/', children_room_view, name='children_room_user'),
    path('advertise/', advertise_view, name='advertise_user'),
    path('mobile_app/', mobile_app, name='mobile_app_user'),
    path('contacts/', contacts_view, name='contacts_user'),
    path('custom_page/', custom_page_view, name='custom_page'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
