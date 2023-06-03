from django.urls import path, include
from .views import *

urlpatterns = [
    path('news/', news, name='news'),
    path('shares/', shares, name='shares'),
    path('list_pages/', list_pages, name='list_pages'),
    path('mailing/', mailing, name='mailing'),
]
