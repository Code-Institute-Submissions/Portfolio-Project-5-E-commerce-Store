from django.shortcuts import render


def view_basket(request):

    """ A view that renders the products in the basket """

    return render(request, "basket/view_basket.html")
