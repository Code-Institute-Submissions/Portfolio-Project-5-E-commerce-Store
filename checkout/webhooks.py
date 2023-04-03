
from django.conf import settings

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.http import require_POST

import stripe

from checkout.webhook_handler import StripeWH_Handler


@csrf_exempt
@require_POST
def webhook(request):
    """ Listen for webhooks from Stripe"""

    # Setup
    wb_secret = settings.STRIPE_WH_SECRET

    stripe.api_key = settings.STRIPE_SECRET_KEY

    event = None

    payload = request.body

    sig_header = request.META['STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    except Exception as e:

        return HttpResponse(content=e, status=400)

    # Handle the event
    print("Success!")

    return HttpResponse(status=200)
