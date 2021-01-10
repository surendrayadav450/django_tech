from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import  Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_prd_by_ids(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})
   