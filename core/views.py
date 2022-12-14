from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import render
import datetime 
from django.utils import timezone
from django.db.models import Q
# Create your views here.
current_datetime = timezone.localtime(timezone.now())

current_date = timezone.now().date()






class CategoryView(APIView):
    def get(self , request , pk=None , format = None):
        try:
            if pk:
                query = Category.objects.filter(id = pk).last()
                if query:
                    serializers = CategorySerializers(query , many = False)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data = {}
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data})
            else:
                queryset = Category.objects.all().order_by("-id")
                if len(queryset)>0:
                    serializers = CategorySerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data =[]
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})

    def post(self, request, format=None):
        try:
            data = request.data
            serializers = CategorySerializers(data=data)
            serializers.is_valid(raise_exception=True)
            serializers.save(is_active=True)
            return JsonResponse({"status":status.HTTP_201_CREATED , "data":serializers.data})
        except Exception as e:
            return JsonResponse(
                {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "msg": e.args[0]}
            )

    def put(self,request, pk, format = None):
        try:
            query = Category.objects.filter(id = pk).last()
            if query:
                
                serializers = CategorySerializers(instance=query , data  = request.data , partial=True)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})
    def delete(self,request, pk, format = None):
        try:
            query = Category.objects.filter(id = pk).last()
            if query:
                query.delete()
                return JsonResponse({"status":status.HTTP_200_OK , "msg":"Category successfully deleted!" })
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})


class CategorySearch(APIView):
    def get(self,request , title):
        try:
            queryset = Category.objects.filter(title__icontains = title)
            if len(queryset)>1:
                    serializers = CategorySerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                data =[]
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})





class DiscountView(APIView):
    def get(self , request , pk=None ,valid = None, format = None):
        try:
            if pk:
                query = Discount.objects.filter(id = pk).last()
                if query:
                    serializers = DiscountSerializers(query , many = False)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data = {}
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data})
            elif valid:
                queryset = Discount.objects.filter( Q(start_date__lte =current_date , end_date__gte = current_date) | Q(start_time__lte = current_datetime ,end_time__gte = current_datetime ))
                
                print(len(queryset))
                if len(queryset)>0:
                    serializers = DiscountSerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data =[]
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })

            else:
                queryset = Discount.objects.all().order_by("-id")
                if len(queryset)>0:
                    serializers = DiscountSerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data =[]
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})

    def post(self, request, format=None):
        try:
            data = request.data
            discount_type = request.data["discount_type"]
            date_type = request.data["date_type"]
            discount_val = request.data["discount_val"]
            start_date = request.data["start_date"]
            end_date = request.data["end_date"]
            start_time = request.data["start_time"]
            end_time = request.data["end_time"]
            if discount_type == "percentage" and discount_val >100 or date_type == "date" and end_date is None and start_date is None or date_type == "time" and start_time is None and end_time is None:
                return JsonResponse({"status":status.HTTP_406_NOT_ACCEPTABLE , "msg":"please Check your data"})
            else:
                serializers = DiscountSerializers(data=data)
                serializers.is_valid(raise_exception=True)
                serializers.save(is_active  =True)
                return JsonResponse({"status":status.HTTP_201_CREATED , "data":serializers.data})
        except Exception as e:
            return JsonResponse(
                {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "msg": e.args[0]}
            )

    def put(self,request, pk, format = None):
        try:
            query = Discount.objects.filter(id = pk).last()
            if query:
                
                serializers = DiscountSerializers(instance=query , data  = request.data , partial=True)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})
    def delete(self,request, pk, format = None):
        try:
            query = Discount.objects.filter(id = pk).last()
            if query:
                query.delete()
                return JsonResponse({"status":status.HTTP_200_OK , "msg":"Discount data successfully deleted!" })
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})



class DiscountSearch(APIView):
    def get(self,request , title):
        try:
            queryset = Discount.objects.filter(title__icontains = title)
            if len(queryset)>1:
                    serializers = DiscountSerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                data =[]
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})


class ProductView(APIView):
    def get(self , request , pk=None , format = None):
        try:
            if pk:
                query = Product.objects.filter(id = pk).last()
                if query:
                    serializers = ProductDetailsSerializers(query , many = False)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data = {}
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data})
            else:
                queryset = Product.objects.all().order_by("-id")
                if len(queryset)>0:
                    serializers = ProductDetailsSerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
                else:
                    data =[]
                    return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})

    def post(self, request, format=None):
        try:
            data = request.data
            serializers = ProductSerializers(data=data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return JsonResponse({"status":status.HTTP_201_CREATED , "data":serializers.data})
        except Exception as e:
            return JsonResponse(
                {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "msg": e.args[0]}
            )

    def put(self,request, pk, format = None):
        try:
            query = Product.objects.filter(id = pk).last()
            if query:
                
                serializers = ProductSerializers(instance=query , data  = request.data , partial=True)
                serializers.is_valid(raise_exception=True)
                serializers.save()
                return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})
    def delete(self,request, pk, format = None):
        try:
            query = Product.objects.filter(id = pk).last()
            if query:
                query.delete()
                return JsonResponse({"status":status.HTTP_200_OK , "msg":"Product successfully deleted!" })
            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND})

        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})


class ProductSearch(APIView):
    def get(self,request , title):
        try:
            queryset = Product.objects.filter(title__icontains = title)
            if len(queryset)>1:
                    serializers = ProductDetailsSerializers(queryset , many = True)
                    return JsonResponse({"status":status.HTTP_200_OK , "data":serializers.data})
            else:
                data =[]
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})


class AssignDiscount(APIView):
    def post(self,request ):
        try:
            data = request.data
            discount_id = request.data["discount"]
            discount_query = Discount.objects.filter(id = discount_id).last()
            product_data = request.data["products"]
            if len(product_data)>0:
                for i in product_data:
                    query = Product.objects.filter(id = i["id"]).last()
                    if query:
                        query.discount = discount_query
                        query.save()
                    else:
                        pass 
                return JsonResponse({"status":status.HTTP_200_OK , "msg":"Discount data updated Successfully !"})

            else:
                return JsonResponse({"status":status.HTTP_404_NOT_FOUND , "data":data })
        except Exception as e:
            return JsonResponse({"status":status.HTTP_500_INTERNAL_SERVER_ERROR , "msg":e.args[0]})



