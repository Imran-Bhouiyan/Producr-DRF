from django.urls import path
from . views import *
from . import views
urlpatterns = [
    # Category
    path("category/" , CategoryView.as_view()),
    path("category_details/<int:pk>/" , CategoryView.as_view()),
    path("category_update/<int:pk>/" , CategoryView.as_view()),
    path("category_delete/<int:pk>/" , CategoryView.as_view()),
    path("category_search/<str:title>/" , CategorySearch.as_view()),
    #Discount
    path("create_discount/" , DiscountView.as_view()),
    path("alldiscount/" , DiscountView.as_view()),
    path("discount_details/<int:pk>/" , DiscountView.as_view()),
    path("discount_update/<int:pk>/" , DiscountView.as_view()),
    path("discount_delete/<int:pk>/" , DiscountView.as_view()),
    path("discount_search/<str:title>/" , DiscountSearch.as_view()),
    #Product

    path("create_product/" , ProductView.as_view()),
    path("allproduct/" , ProductView.as_view()),
    path("product_details/<int:pk>/" , ProductView.as_view()),
    path("product_update/<int:pk>/" , ProductView.as_view()),
    path("product_delete/<int:pk>/" , ProductView.as_view()),
    path("product_search/<str:title>/" , ProductSearch.as_view()),
    path("assign_discount/" , AssignDiscount.as_view()),
   
]

