# from django.http import HttpResponse
# from django.shortcuts import render

# from carton.cart import Cart
# from product.models import Product

# def add(request):
#     cart = Cart(request.session)
#     product = Product.objects.get(id=request.GET.get('sku'))
#     cart.add(product, price=product.price)
#     return HttpResponse("Added")

# def show(request):
#     return render(request, 'shopping/show-cart.html')