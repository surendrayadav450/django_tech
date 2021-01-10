from django.shortcuts import render,HttpResponse,redirect
from store.models.product import Product
from store.models.category import Category
from store.models.customer import  Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View



class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)

        errormessage = self.validation(customer)

        data = {'error': errormessage,
                'values': values
                }
        if not errormessage:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            return render(request, 'signup.html', data)
    def validation(self,customer):
        # validation
        errormessage = None
        if (not customer.first_name):
            errormessage = "first name cant be empty"
        elif len(customer.first_name) < 4:
            errormessage = "first name should be longer 4 character"
        # elif Customer.isExists:
        #     errormessage = "Email already exists"
        return errormessage




