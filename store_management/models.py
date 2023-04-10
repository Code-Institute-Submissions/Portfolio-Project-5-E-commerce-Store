from django.db import models

from django.contrib.auth.models import User

from products.models import Product

from checkout.models import Order


class Comment(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='comments')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', null=True)

    title = models.CharField(max_length=30, null=False, blank=False)

    user_name = models.CharField(max_length=20, null=False, blank=False)

    content = models.TextField(max_length=500, null=False, blank=False)

    posted_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    class Meta:

        ordering = ['posted_on']

    def __str__(self):

        return str(self.content) + ' by ' + str(self.user_name)


class Newsletter(models.Model):

    email_address = models.EmailField(null=True)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.email_address


class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=254, null=True)

    email_address = models.EmailField(null=True)

    tel_number = models.CharField(max_length=30, null=True, blank=True)

    message = models.TextField(null=True)

    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name
