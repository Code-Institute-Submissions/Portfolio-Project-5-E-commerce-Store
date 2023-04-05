from django.shortcuts import render, get_object_or_404

from .models import UserProfile

from .forms import UserProfileForm

from django.contrib import messages


def view_profile(request):

    """A view that renders the user profile"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':

        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():

            form.save()

            messages.info(request, " Profile updated succefully")

    form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profile_management/view_profile.html'

    context = {

        'form': form,

        'orders': orders,
    }

    return render(request, template, context)
