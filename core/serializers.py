from rest_framework import serializers
from .models import * 

import datetime 
from django.utils import timezone

# Create your views here.
current_datetime = timezone.localtime(timezone.now())

current_date = timezone.now().date()

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {'title':{"required":True} }


class DiscountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"
        extra_kwargs = {'title':{"required":True},
         'discount_type':{"required":True}
         }

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {'title':{"required":True}, 'category':{"required":True} ,'old_price':{"required":True}  }



class ProductDetailsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    discount = DiscountSerializers()
    current_price = serializers.SerializerMethodField(method_name='get_new_prices')
    class Meta:
        model = Product
        fields = ("id" , "title" , "old_price" , "current_price", "category" , "discount" )
       

    def get_new_prices(self,instance):
        try:
            if instance.discount.date_type == "date" and instance.discount.start_date <= current_date and instance.discount.end_date >= current_date:
                price = instance.new_price 
            elif instance.discount.date_type == "time" and instance.discount.start_time <= current_datetime and instance.discount.end_time >= current_datetime:
                price = float(instance.new_price)
            else:
                price = float(instance.new_price)
        except:
            price = float(instance.old_price)
        return price

 



# class ProductDetailsSerializers(serializers.ModelSerializer):
#     category_details = serializers.SerializerMethodField(method_name='get_category')
#     discount_details = serializers.SerializerMethodField(method_name='get_discount')
#     current_price = serializers.SerializerMethodField(method_name='get_new_prices')
#     class Meta:
#         model = Product
#         fields = ("id" , "title" , "old_price" , "current_price", "category_details" , "discount_details" )
       

#     def get_new_prices(self,instance):
#         try:
#             if instance.discount.date_type == "date" and instance.discount.start_date >= current_date and instance.discount.end_date <= current_date:
#                 price = instance.new_price 
#             elif instance.discount.date_type == "time" and instance.discount.start_time >= current_datetime and instance.discount.end_time <= current_datetime:
#                 price = float(instance.new_price)
#             else:
#                 price = float(instance.new_price)
#         except:
#             price = float(instance.old_price)
#         return price


#     def get_category(self,instance):
#         try:
#             query = Category.objects.filter(id = instance.id).last()
#             serializers = CategorySerializers(query , many = False)
#             data = serializers.data
#         except:
#             data = {}
#         return data


#     def get_discount(self,instance):
#         try:
#             query = Discount.objects.filter(id = instance.id).last()
#             serializers = DiscountSerializers(query , many = False)
#             data = serializers.data
#         except:
#             data = {}
#         return data


