from django.shortcuts import render
import os


def index(request):
    """A view render's the home page"""

    return render(request, "home/index.html")
