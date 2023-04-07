from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category_name', 'slug',)

    prepopulated_fields = {'slug': ('category_name',)}


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'model_name', 'category', 'description', 'slug', 'size', 'image', 'price',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
