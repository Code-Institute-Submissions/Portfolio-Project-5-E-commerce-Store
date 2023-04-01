from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

from django.contrib import messages

from basket.contexts import basket_contents

import stripe

from django.conf import settings


def checkout(request):
    """ A view that renders the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, " There's nothing in your basket!")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total_amount = current_basket['order_total']
    stripe_total = round(total_amount * 100)

    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(

        amount=stripe_total,

        currency=settings.STRIPE_CURRENCY,

    )
    if not stripe_public_key:
        messages.warning(request, "Stripe Public key missing, did you forget \
             to set variable?")

    order_form = OrderForm()
    context = {
        'order_form':  order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,

    }

    return render(request, 'checkout/checkout.html', context)
