from django.urls import path, include

from .views import *
from cinema.views import list_cinemas
from core.views import news_view, add_news, edit_news, delete_news, shares_view, add_shares, edit_shares, \
    delete_shares, list_pages, create_page, edit_pages, delete_page, add_contact, mailing_view

urlpatterns = [
    path('statistic/', base_admin, name='statistic_admin'),
    path('banners/', banners_view, name='banners_admin'),
    path('list_films/', list_films, name='list_films_admin'),
    path('list_films/edit_film/<int:pk>/', edit_films, name='edit_films_admin'),
    path('list_cinemas/', list_cinemas, name='list_cinemas_admin'),
    path('news/', news_view, name='news_admin'),
    path('news/add_news/', add_news, name='add_news'),
    path('news/edit_news/<int:pk>', edit_news, name='edit_news'),
    path('news/delete_news/<int:pk>', delete_news, name='delete_news'),
    path('shares/', shares_view, name='shares_admin'),
    path('shares/add_shares/', add_shares, name='add_shares'),
    path('shares/edit_shares/<int:pk>', edit_shares, name='edit_shares'),
    path('shares/delete_shares/<int:pk>', delete_shares, name='delete_shares'),
    path('list_pages/', list_pages, name='list_pages_admin'),
    path('list_pages/create_page/', create_page, name='create_page'),
    path('list_pages/<str:name_page>/', edit_pages, name='edit_pages'),
    path('list_pages/<str:name_page>/add_contact/', add_contact, name='add_contact'),
    path('list_pages/delete_page/<int:id_page>/', delete_page, name='delete_page'),
    path('mailing/', mailing_view, name='mailing_admin'),
    path('list_users/', list_users, name='list_users_admin'),
    path('list_users/<int:pk>/', edit_user, name='edit_user'),
    path('list_users/delete_user/<int:pk>/', delete_user, name='delete_user'),
    path('profile/', profile_view, name='profile_admin'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
