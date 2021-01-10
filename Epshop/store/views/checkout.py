from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import  Customer
from store.models.order import  Order
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class Checkout(View):
    def post(self,request):
       address = request.POST.get('address')
       phone = request.POST.get('phone')
       customer = request.session.get('customer')

       cart = request.session.get('cart')
       products = Product.get_prd_by_ids(list(cart.keys()))
       print(address, phone, customer,cart,products)
       for product in products:
           order = Order(customer = Customer(id=customer),
                         product = product,
                         price = product.Price,
                         address = address,
                         phone = phone,
                         quantity = cart.get(str(product.id)))
           request.session['cart']={}
           order.placeOrder()
       return redirect('cart')
   