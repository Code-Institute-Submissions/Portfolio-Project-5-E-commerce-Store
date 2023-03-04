from django.shortcuts import render, get_object_or_404

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


def product_detail(request, slug):
    """ A view that displays all product to customers"""

    product = get_object_or_404(Product, slug=slug)

    context = {
        'product': product,
    }

    return render(request, "products/product_detail.html", context)
