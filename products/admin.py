from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category_name', 'slug',)

    prepopulated_fields = {'slug': ('category_name',)}


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'slug', 'size', 'image', 'price',)

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
