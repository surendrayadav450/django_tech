from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import  Customer
from store.models.order import  Order
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class orderview(View):
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_order_buy_cust_id(customer)
        orders = orders.reverse()
        # print(orders)
        return render(request,'orders.html',{'orders':orders})
   