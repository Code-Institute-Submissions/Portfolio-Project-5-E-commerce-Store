from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.contrib import messages

from .forms import ProductForm

from products.models import Product, Category


def add_product(request):

    """ Add's products to the store """

    if request.method == 'POST':

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.info(request, 'Product added successfully!')

            return redirect(reverse('add_product'))

        else:

            messages.error(request, 'Unable to add product.\
                            Please check form is valid.')

    else:

        form = ProductForm()

    context = {

        'form': form,
    }

    return render(request, 'store_management/add_product.html', context)