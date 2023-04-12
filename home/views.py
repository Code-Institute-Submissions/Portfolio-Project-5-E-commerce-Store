from django.shortcuts import render

from store_management.models import Newsletter

from store_management.forms import NewsletterForm


def index(request):
    """A view render's the home page"""

    return render(request, "home/index.html")
