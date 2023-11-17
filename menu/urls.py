from django.urls import path
from .views import get_menu


urlpatterns = [
    path('<slug:menu_slug>/', get_menu, name='get_menu'),
]
