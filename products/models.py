from django.db import models


class Category(models.Model):

    category_name = models.CharField(max_length=254, db_index=True)

    slug = models.SlugField(max_length=254, unique=True)

    class Meta:

        verbose_name_plural = "categories"

    def __str__(self):

        return self.category_name


class Product(models.Model):

    name = models.CharField(max_length=254)

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=254)

    size = models.CharField(max_length=5)

    image = models.ImageField(null=True, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    date = models.DateField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "products"

    def __str__(self):

        return self.name