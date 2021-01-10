from django.contrib import admin
from .models import Product,Category,Customer,Order



class AdminProduct(admin.ModelAdmin):
    list_display = ['name','Price','category']
class AdminCategory(admin.ModelAdmin):
     list_display = ['name']


admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)


# Register your models here.
