from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('category_name',)

    readonly_fields = ('slug',)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'model_name', 'category', 'description', 'size', 'image', 'price',)

    readonly_fields = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
