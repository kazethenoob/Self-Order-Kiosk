from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('category/<slug:category_slug>/', views.menu_list, name='menu_by_category'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:item_id>/', views.cart_add, name='cart_add'),
    path('cart/increment/<int:item_id>/', views.cart_increment, name='cart_increment'),
    path('cart/decrement/<int:item_id>/', views.cart_decrement, name='cart_decrement'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
]

    # ... other URL patterns ...
