from django.urls import path, include

from .views import *

urlpatterns = [
    path('statistic/', base_admin, name='statistic'),
    path('banners/', banners, name='banners'),
    path('list_users/', list_users, name='list_users'),
    path('profile/', profile, name='profile'),
    path('login/',  login, name='login'),
    path('register/',  register, name='register'),
]
