from decimal import Decimal
from django.shortcuts import render, redirect
from .models import Order, OrderItem
from menu.cart import Cart  # Assuming your Cart class is in cart/cart.py

def place_order(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect('menu_list')  # Redirect if cart is empty

    order = Order.objects.create()
    order_items = []
    total_price = Decimal('0.00')
    for item in cart:
        order_item = OrderItem.objects.create(
            order=order,
            menu_item=item['item'],
            quantity=item['quantity']
        )
        item_total = item['price'] * item['quantity']
        total_price += item_total
        order_items.append({
            'name': item['item'].name,
            'quantity': item['quantity'],
            'price': item['price'],
            'total': item_total
        })

    cart.clear()  # Clear the cart session
    return render(request, 'orders/order_receipt.html', {
        'order': order,
        'order_items': order_items,
        'total_price': total_price
    })
