from django.conf import settings

from decimal import Decimal


def bag_contents(request):

    """ Basket contents """

    basket_items = []

    total = 0

    product_count = 0

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    order_total = delivery + total

    context = {

        'basket_items': basket_items,

        'product_count': product_count,

        'delivery': delivery,

        'order_total': order_total,

    }
