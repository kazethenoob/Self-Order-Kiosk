from decimal import Decimal
from .models import MenuItem

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    # ... [other methods] ...

    def add(self, item, quantity=1):
        item_id = str(item.id)
        if item_id in self.cart:
            self.cart[item_id]['quantity'] += quantity
        else:
            self.cart[item_id] = {'quantity': quantity, 'price': str(item.price)}
        self.save()

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def increment(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            self.cart[item_id]['quantity'] += 1
            self.save()

    def decrement(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            if self.cart[item_id]['quantity'] > 1:
                self.cart[item_id]['quantity'] -= 1
            else:
                self.remove(item)
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        item_ids = self.cart.keys()
        items = MenuItem.objects.filter(id__in=item_ids)
        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item
        for data in cart.values():
            data['price'] = Decimal(data['price'])
            data['total_price'] = data['price'] * data['quantity']
            yield data

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
