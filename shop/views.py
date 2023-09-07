from django.shortcuts import render
from django.views import View
from .models import *


# Create your views here.
class Home(View):
    def get(self, request):
        return render(request, 'home/index.html')

class Shop(View):
    def get(self, request):
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'shop/index.html', context)

class Cart(View):
    def get(self, request):
        return render(request, 'cart.html')

class Checkout(View):
    def get(self, request):
        return render(request, 'checkout.html')
