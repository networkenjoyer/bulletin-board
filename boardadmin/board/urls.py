from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'search_adv'),
    path('addadv/', addadv, name = 'about'),
]