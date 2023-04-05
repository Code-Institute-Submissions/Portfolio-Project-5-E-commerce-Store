from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def view_profile(request):

    """A view that renders the user profile"""

    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profile_management/view_profile.html'

    context = {

        'profile': profile,
    }

    return render(request, template, context)
