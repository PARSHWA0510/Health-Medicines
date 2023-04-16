from unicodedata import category
from django.db import models
import secrets
import string
class Auth_User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="user_profile",default="user_profile/default.png")

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    discription=models.CharField(max_length=100,default='',null=True,blank=True)
    price=models.IntegerField(default=0,null=False)
    off_price=models.IntegerField(default=0,null=False)
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='product_details',default="user_profile/default.png")
    
    def __str__(self):
        return self.name
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    def get_products_by_category(category_name):
        if category_name:
            return Product.objects.filter(category=category_name)
        else:
            return Product.objects.all()
    def get_products_by_id(id):
        return Product.objects.filter(id=id).first()


class Cart_Item(models.Model):
    cart_no = models.CharField(default="N/A",max_length=100)
    product_name = models.CharField(max_length=200)
    product_price = models.CharField(max_length=10)
    time_added = models.DateTimeField(auto_now_add=True)
    total_ord = models.CharField(max_length=3,default="0")
    total_price = models.CharField(max_length=5,default="0")
    product_id = models.CharField(max_length=13,default="-1")
    image = models.TextField(max_length=150,default="user_profile/default.png")
    def __str__(self): return self.product_name+"->"+str(self.cart_no)
    # @staticmethod
    # def get_cart(id):
    #     Cart.objects.filter(user_id=id).first()




