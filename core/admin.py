from django.contrib import admin
from .models import *
@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'id',
        'title',
        'is_active',
    )
    list_filter = (
        'id',
        'title',
        'is_active',
     
    )



@admin.register(Discount)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'id',
        'title',
        'is_active',
    )
    list_filter = (
        'id',
        'title',
        'is_active',
     
    )


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = (
        'id',
        'category',
        'discount',
    )
    list_filter = (
        'id',
        'category',
        'discount',
     
    )
