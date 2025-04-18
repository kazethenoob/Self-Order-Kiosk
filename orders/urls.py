from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # ... other URL patterns ...
    path('place-order/', views.place_order, name='place_order'),
]
