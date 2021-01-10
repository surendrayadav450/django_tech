from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=200)



    def register(self):
        self.save()


    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False




    @staticmethod
    def get_customer_byemail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False