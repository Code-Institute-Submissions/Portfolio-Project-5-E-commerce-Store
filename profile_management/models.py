from django.db import models

from django.db.models.signals import post_save

from django.dispatch import receiver

from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):

    """
    A user profile model for maintaining default
    delivery information, update user details and
    order history.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_phone_number = models.CharField(max_length=30, null=True, blank=True)

    default_address1 = models.CharField(max_length=254, null=True, blank=True)

    default_address2 = models.CharField(max_length=254, null=True, blank=True)

    default_city = models.CharField(max_length=254, null=True, blank=True)

    default_county = models.CharField(max_length=254, null=True, blank=True)

    default_postal_code = models.CharField(max_length=50, null=True, blank=True)

    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):

        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update the user profile"""

    if created:
        UserProfile.objects.create(user=instance)

    instance.userprofile.save()
