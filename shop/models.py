from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    mobile_number = models.CharField(max_length=12)
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address_line1 = models.TextField()

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique= True)


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length= 200)
    product_description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    product_image = models.ImageField(upload_to = 'product_img/')
    category = models.ForeignKey('Category', on_delete= models.CASCADE, verbose_name= 'Category')



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('Product', on_delete= models.CASCADE, verbose_name= 'Product')
    quantity = models.CharField(max_length=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete= models.CASCADE, verbose_name= 'Customer', default=None)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('Product', on_delete= models.CASCADE, verbose_name= 'Product')
    customer= models.ForeignKey('Customer', on_delete= models.CASCADE, verbose_name= 'Customer')
    quantity = models.CharField(max_length=2)
    delivery = models.TextField(verbose_name='Delivery Address')
