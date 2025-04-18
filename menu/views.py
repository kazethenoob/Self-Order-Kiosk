from django.shortcuts import render
from .models import MenuItem, Category
from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart

def menu_list(request, category_slug=None):
    categories = Category.objects.all()
    category = None
    menu_items = MenuItem.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        menu_items = menu_items.filter(category=category)

    context = {
        'categories': categories,
        'menu_items': menu_items,
        'active_category': category,
    }
    return render(request, 'menu/menu_list.html', context)



def cart_detail(request):
    cart = Cart(request)
    return render(request, 'menu/cart_detail.html', {'cart': cart})

def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    cart.add(item=item)
    return redirect('cart_detail')

def cart_increment(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    cart.increment(item)
    return redirect('cart_detail')

def cart_decrement(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    cart.decrement(item)
    return redirect('cart_detail')

def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(MenuItem, id=item_id)
    cart.remove(item)
    return redirect('cart_detail')



# Create your views here.
