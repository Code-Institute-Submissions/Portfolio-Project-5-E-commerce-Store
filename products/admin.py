from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category_name',)

    readonly_fields = ('slug',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'model_name', 'category', 'description', 'size', 'image', 'price',)

    readonly_fields = ('slug',)


