from django.shortcuts import render

from .models import Product, Category


def all_products(request):
    """ A view that displays all product to customers"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/products.html", context)


def all_categories(request):

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return context
