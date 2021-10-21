from django.conf import settings
from decimal import Decimal
from product.models import ProductPage, ProductIndexPage

class Cart(object):
    def __init__(self, request):
        self.session=request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}

        self.cart=cart


    def add(self, product, quantity=1, override_quantity=False):
        product_sku = str(product.sku)
        if product_sku not in self.cart:
            self.cart[product_sku]={'quantity':0, 'price':str(product.price)}

        if override_quantity:
            self.cart[product_sku]['quantity']=quantity
        else:
            self.cart[product_sku]['quantity'] += quantity
        self.save()


    def save(self):
        self.session.modified = True


    def remove(self, product):
        product_sku = str(product.sku)
        if product_sku in self.cart:
            del self.cart[product_sku]
            self.save()


    def __iter__(self):
        product_skus = self.cart.keys()
        products = ProductPage.objects.filter(id__in=product_skus)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.sku)]['product'] = product

        for item in cart.values():
            item['price']=Decimal(item['price'])
            item['total_price']=item['price'] * item['quantity']
            yield item


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    
    def get_total_price(self):
        return sum(Decimal(item['price'] * item['quantity'] for item in self.cart.values()))


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()