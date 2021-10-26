from django.shortcuts import get_object_or_404, render, redirect
from .cart import Cart
from .forms import CartAddProductForm
from product.models import ProductPage
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_sku):
    cart = Cart(request)
    product = get_object_or_404(ProductPage, sku=product_sku)
    form = CartAddProductForm(request.POST)
    print(product.url)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('shopping_cart:cart_detail')


def cart_remove(request, product_sku):
    cart = Cart(request)
    product = get_object_or_404(ProductPage, sku=product_sku)
    cart.remove(product)
    return redirect('shopping_cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shopping_cart/detail.html', {'cart': cart.cart, 'total': cart.get_total_price()})