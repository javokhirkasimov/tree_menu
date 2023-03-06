from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
    # path('cars/lambo/', index, name='lambo'), # This is a test
]
