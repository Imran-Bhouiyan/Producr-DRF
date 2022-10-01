from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.


class Discount(models.Model):
    type_choices = (
        ("percentage","percentage"),
        ("amount","amount"),
        ("date","date"),
        ("time","time"),
    )

    title = models.CharField(max_length=50 , unique=True)
    discount_type = models.CharField(max_length=15 , choices = type_choices)
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
    discount= models.ForeignKey(Discount , on_delete = models.CASCADE)
    old_price = models.FloatField(default = 0)
    new_price = models.FloatField(default = 0 , null = True , blank=True)

    def __str__(self):
        return str(self.title) 

    class Meta:
        db_table = 'Product'
        managed = True
