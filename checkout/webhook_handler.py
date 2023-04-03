from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle's Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle's all generic/unknown/unexpected webhook event """

        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle's the payment_intent.success webhook from stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """ Handle's the payment_intent.failed webhook from stripe """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
