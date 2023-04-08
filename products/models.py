from django.db import models

from django.shortcuts import reverse

from django.utils.text import slugify

from .fields import CaseInsensitiveCharField

from django.core.validators import RegexValidator


product_sizes = (

    ('4 x 6 inches', '4 x 6 inches'),
    ('5 x 7 inches', '5 x 7 inches'),
    ('8 x 10 inches', '8 x 10 inches'),
    ('8.5 x 11 inches', '8.5 x 11 inches'),
)

# This line Code (alphanumeric) is from Martin peters Stack overflow
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')


class Category(models.Model):

    category_name = CaseInsensitiveCharField(max_length=254, db_index=True, unique=True, validators=[alphanumeric])

    slug = models.SlugField(max_length=254, blank=False, null=False, db_index=True)

    class Meta:

        verbose_name_plural = "categories"

    def __str__(self):

        return self.category_name

    def get_absolute_url(self):

        return reverse('search_category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)


class Product(models.Model):

    name = CaseInsensitiveCharField(max_length=254, unique=True, validators=[alphanumeric])

    model_name = models.CharField(max_length=254, blank=True, null=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=254, blank=False, null=False, db_index=True)

    size = models.CharField(max_length=20, choices=product_sizes, default='4 x 6 inches')

    image = models.ImageField(null=False, blank=False)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    date = models.DateField(auto_now_add=True)

    class Meta:

        verbose_name_plural = "products"

    def __str__(self):

        return self.name

    def get_absolute_url(self):

        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
