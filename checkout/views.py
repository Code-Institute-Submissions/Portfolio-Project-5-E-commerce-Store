from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

from django.contrib import messages

from basket.contexts import basket_contents

import stripe

from django.conf import settings


def checkout(request):
    """ A view that renders the checkout page """
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, " There's nothing in your basket!")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total_amount = current_basket['order_total']
    stripe_total = round(total_amount * 100) 

    order_form = OrderForm()
    context = {
        'order_form':  order_form,
        'stripe_public_key': 'pk_test_51MrJd0BGDHfprW8z3bqOZqLBq6T2NHn13DBJsPabsLipFJrq9h1eWv82KkhfFyzw1bDSkBtijETsuM0zGxjtD1LX001sxITvmY',
        'client_secret': 'test client secret',

    }

    return render(request, 'checkout/checkout.html', context)
