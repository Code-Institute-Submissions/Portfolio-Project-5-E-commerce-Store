from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from . models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_on_save(send, intance, created, **kwargs):
    """ Updates the order total on orderitem create/updated"""

    instance.order.update_total()


@receiver(post_delete, sender=OrderItem)
def update_on_save(send, intance, **kwargs):
    """ Updates the order total on orderitem delete """

    instance.order.update_total()