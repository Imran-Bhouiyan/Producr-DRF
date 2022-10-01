from rest_framework import serializers
from .models import * 



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