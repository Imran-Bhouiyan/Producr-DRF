from email.policy import default
from unicodedata import category
from django.db import models


import datetime 
from django.utils import timezone

# Create your views here.
current_datetime = timezone.localtime(timezone.now())

current_date = timezone.now().date()

# Create your models here.


class Discount(models.Model):
    type_choices = (
        ("percentage","percentage"),
        ("amount","amount"),

    )
    date_choices = (
        ("date","date"),
        ("time","time"),  
    )

    title = models.CharField(max_length=50 , unique=True)
    discount_type = models.CharField(max_length=15 , choices = type_choices)
    date_type = models.CharField(max_length=15 , choices = date_choices)
    discount_val = models.FloatField(default=0)
    start_date = models.DateField(auto_now_add=True , null = True , blank = True)
    end_date = models.DateField( null = True , blank = True)
    start_time = models.DateTimeField(auto_now_add=True , null = True , blank = True)
    end_time = models.DateTimeField( null = True , blank = True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title) 

    class Meta:
        db_table = 'Discount'
        managed = True


class Category(models.Model):
    title = models.CharField(max_length=50 , unique=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return str(self.title) 

    class Meta:
        db_table = 'Category'
        managed = True


class Product(models.Model):
    title = models.CharField(max_length=255)
    category= models.ForeignKey(Category , on_delete = models.CASCADE)
    discount= models.ForeignKey(Discount , on_delete = models.CASCADE , null=True , blank = True)
    old_price = models.FloatField(default = 0)
    new_price = models.FloatField(default = 0 , null = True , blank=True)

    def __str__(self):
        return str(self.title) 
    @property
    def price(self):
        if self.discount.discount_type == "percentage":
            per_val = float(self.discount.discount_val * self.old_price)/100
            new_price = float(self.old_price) - per_val
            return new_price 
        else: 
            per_val = float(self.discount.discount_val * self.old_price)/100
            new_price = float(self.old_price) - float(self.discount.discount_val)
            return new_price
        

    def save(self, *args, **kwargs):
        self.new_price = self.price
        super(Product, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Product'
        managed = True
