from django.db import models

from django.shortcuts import reverse


product_sizes = (

    ('4X6IN (10X15CM)', '4X6IN (10X15CM)'),
    ('5X7IN (13X18CM)', '5X7IN (13X18CM)'),
    ('8X10IN (20X25CM)', '8X10IN (20X25CM)'),
)


class Category(models.Model):

    category_name = models.CharField(max_length=254, db_index=True)

    slug = models.SlugField(max_length=254, unique=True)

    class Meta:

        verbose_name_plural = "categories"

    def __str__(self):

        return self.category_name

    def get_absolute_url(self):

        return reverse('search_category', args=[self.slug])


class Product(models.Model):

    name = models.CharField(max_length=254)

    model_name = models.CharField(max_length=254, blank=True, null=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=254)

    size = models.CharField(max_length=20, choices=product_sizes, default='4X6IN (10X15CM)')

    image = models.ImageField(null=True, blank=True)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    date = models.DateField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "products"

    def __str__(self):

        return self.name

    def get_absolute_url(self):

        return reverse('product_detail', args=[self.slug])
