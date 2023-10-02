from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import *

urlpatterns = [
    path('', index, name = 'search_adv'),
    path('addadv/', addadv, name = 'add_adv'),
    path('adv/<int:pk>/', views.CardDetailView.as_view(), name = 'adv')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)