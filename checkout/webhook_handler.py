from django.http import HttpResponse

from products.models import Product

from .models import Order, OrderItem

import time

import json


class StripeWH_Handler:
    """ Handle's Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle's all generic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle's the payment_intent.success webhook from stripe """

        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_details = intent.metadata.save_details

        # Get Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.lastest_charge
        )

        billing_details = stripe_charge.billing_details

        shipping_details = intent.shipping

        order_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details

        for field, value in shipping_details.address.item():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False

        attempt = 1

        while attempt <= 5:

            try:

                order = Order.object.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postal_code__iexact=shipping_details.address.postal_code,
                    order_total=order_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True

                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

            if order_exists:

                return HttpResponse(
                    content=f'Webhook received: {event["type"]}\
                        | SUCCESS: Verified order already in database',
                    status=200)
            else:

                order = None

                try:

                    order = Order.objects.create(

                        full_name__iexact=shipping_details.name,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        address1=shipping_details.address.line1,
                        address2=shipping_details.address.line2,
                        city=shipping_details.address.city,
                        county=shipping_details.address.state,
                        postal_code=shipping_details.address.postal_code,
                        original_basket=basket,
                        stripe_pid=pid,

                    )

                    for product_id, product_quantity in json.loads(basket).items():

                        product = get_object_or_404(Product, id=product_id)

                        if isinstance(product_quantity, int):

                            order_item = OrderItem(

                                order=order,

                                quantity=product_quantity,

                                product=product,

                            )
                            order_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(content=f'Webhook received: \
                        {event["type"]}| ERROR: {e}', status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS:\
                 Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle's the payment_intent.failed webhook from stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
