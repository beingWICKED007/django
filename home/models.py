from ast import mod
from random import choices
from re import S
from secrets import choice
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Price(models.Model):

    filter_price = {
        ('0 To 100', '0 To 100'),
        ('100 To 200', '100 To 200'),
        ('200 To 300', '200 To 300'),
        ('300 To 400', '300 To 400'),
        ('400 To 500', '400 To 500'),
      }
    price = models.CharField( choices=filter_price, max_length=100)

    def __str__(self) -> str:
        return self.price



class Color(models.Model):
    name = models.CharField(max_length=255)
    color_id = models.CharField(max_length=100)
    color_class = models.CharField(max_length=255)
    color_for = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Size(models.Model):
    name = models.CharField(max_length=255)
    size_id = models.CharField(max_length=255)
    size_for = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



class Product(models.Model):
    STATUS = ('Publish', 'Publish'),('Draft','Draft')
    STOCK = ('In stock', 'In stock'),('Out Of Stock','Out Of Stock')
    
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=255)
    price = models.IntegerField()
    descounted_price = models.IntegerField()
    image = models.ImageField(upload_to = 'Images/product')
    description = models.TextField()
    status = models.CharField(choices =STATUS, max_length=100)
    stock = models.CharField(choices=STOCK, max_length=100)


    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Price, on_delete=models.CASCADE,null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name



class Cart(models.Model):
	user = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 400)
	items = models.ForeignKey(Product,on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)
	checkout = models.BooleanField(default = False)
	total = models.IntegerField(default = 0)

	def __str__(self):
		return self.user




class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name




class Otp(models.Model):
    user = models.CharField(max_length=255)
    code = models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.user


class HomeCategories(models.Model):
    STATUS = ('active','active',),('blank','blank')
    name = models.CharField(max_length=255)
    data_filter = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS,max_length=255)
    
    def __str__(self) -> str:
        return self.name

# class HomeSubCategories(models.Model):
#     STATUS = ('active','active',),('blank','blank')
#     name = models.CharField(max_length=255)
#     data_filter = models.CharField(max_length=255)
#     status = models.CharField(choices=STATUS,max_length=255)
    
    def __str__(self) -> str:
        return self.name

class HomeProduct(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Images/homeproduct')
    price = models.IntegerField()
    category = models.ForeignKey(HomeCategories,on_delete=models.CASCADE)
    # subcategory = models.ForeignKey(HomeSubCategories,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



    





