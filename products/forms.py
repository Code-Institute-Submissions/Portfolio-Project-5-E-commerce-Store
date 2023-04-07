from django import forms

from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = '__all__'

        exclude = ('date')

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'name': 'Name',

            'model_name': 'Model Name',

            'category': 'Category',

            'description': 'Description',

            'slug': 'Slug',

            'size': 'Size',

            'image': 'Image',

            'price': 'Price',
        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False
