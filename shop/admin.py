from django.contrib import admin
from . models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_description','price','product_image','categories')
    raw_id_fields = ['category']
    def categories(self,obj):
        return obj.category.name
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','last_name','mobile_number','email', 'address_line1')
    