from django.db import models
from django.contrib.auth.models import User

class CatagoryItems(models.Model):
    heading = models.CharField(max_length=50, default="")
    offer = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", max_length=250, null=True, default=None)

    def __str__(self):
        return self.heading


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/", max_length=250, null=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    country = models.CharField(max_length=100)
    address = models.TextField()
    state =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    zipcode = models.IntegerField()
    total_amount = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    payment_id = models.CharField(max_length=50, null=True, blank=True)
    paid = models.BooleanField(default=0, null=True, blank=True)


    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/order_image", max_length=250, null=True, default=None)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=1000)

    def __str__(self):
        return self.order.user.username
    
    
class Review(models.Model):
    image =  models.ImageField(upload_to="images/", max_length=250, null=True, default=None)
    name = models.CharField(max_length=50, default="")
    comment = models.TextField()
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name