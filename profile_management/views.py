from django.shortcuts import render


def view_profile(request):

    """A view that renders the user profile"""

    template = 'profile_management/view_profile.html'

    context = {

    }

    return render(request, template, context)
