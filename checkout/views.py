from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import OrderForm, Order

from django.contrib import messages

from basket.contexts import basket_contents

import stripe

from django.conf import settings

from .models import OrderItem

from products.models import Product


def checkout(request):
    """ A view that renders the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':

        basket = request.session.get('basket', {})

        form_data = {

            'full_name': request.POST['full_name'],

            'email': request.POST['email'],

            'phone_number': request.POST['phone_number'],

            'address1': request.POST['address1'],

            'address2': request.POST['address2'],

            'city': request.POST['city'],

            'county': request.POST['county'],

            'country': request.POST['country'],

            'postal_code': request.POST['postal_code'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():

            order = order_form.save()

            for product_id, product_quantity in basket.items():

                try:

                    product = get_object_or_404(Product, id=product_id)

                    order_item = OrderItem(

                        order=order,

                        quantity=quantity,

                        product=product,

                    )
                except Product.DoesNotExit:

                    messages.error(request, " We're Sorry! One of the product \
                         in your basket was not found in our database, please \
                        contact for help!")

                    order.delete()

                    return redirect(reverse('view_basket'))

            request.session['save-details'] = 'save-details' in request.POST

            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, "There was an error when submiting the\
             form. Please check the details you have provided. ")

    else:

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


def checkout_success(request, order_number):
    """ This view is used for successful checkouts"""

    save_details = request.session.get('save-details')

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f"Thank you for ordering. We received your order \
         and will begin processing it soon. YOUR ORDER NO. {order_number}. A \
            confirmation email will be sent to {order.email}.")

    if 'basket' in request.session:

        del request.session['basket']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
