from django.urls import path
from .views import place_order,hello

urlpatterns = [
    path('orders/', place_order, name='place_order'),
    path('hello', hello, name='hello'),
]
