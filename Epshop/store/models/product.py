from django.db import models
from .category import Category


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    Price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default="")
    Date = models.DateField()
    image = models.ImageField(upload_to="upload/products/", default="")

    def __str__(self):
        return self.name

    @staticmethod
    def get_prd_by_ids(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    def get_product_catogry_byid(categoryid):
        if categoryid:
            return Product.objects.filter(category=categoryid)
        else:
            return Product.get_all_product()

