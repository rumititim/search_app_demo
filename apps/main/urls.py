from django.conf.urls import url
from django.urls import path

from .views import search

urlpatterns = [
    path('search/<str:query>/', search, name='search'),
    path('search/', search, name='search'),
]