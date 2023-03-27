from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

from django.contrib import messages


def checkout(request):
    """ A view that renders the checkout page """
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, " There's nothing in your basket!")
        return redirect(reverse('products'))

    order_form = Orderform()
    context = {
        'order_form':  order_form,
    }

    return render(request, 'checkout/checkout.html', context)
