from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import  Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View

class index(View):

    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            qantity=cart.get(product)
            # print(qantity,12)
            if qantity:
                if remove:
                    if qantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=qantity-1
                else:
                    cart[product] = qantity + 1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        print(request.session['cart'])
        return redirect('homepage')
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        # request.session.get('cart').clear();
        categories = Category.get_all_catogries()
        data = {}
        categoryid = request.GET.get('category')  # get  category id when we will click

        if categoryid:
            products = Product.get_product_catogry_byid(categoryid)
        else:

            products = Product.get_all_product()
        # return render(request,'order/order.html',{'all_products':all_products})
        data['products'] = products
        data['categories'] = categories
        # print(request.session.get('email'))
        return render(request, 'index.html', data)


