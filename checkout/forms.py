from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = ('full_name', 'email', 'phone_number', 'country', 'address1', 'address2', 'city', 'county', 'postal_code',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders and  set autofoucs to first field"""

        super().__init__(*args, **kwargs)
        placeholders = {

            'full_name': 'Full Name',

            'email': 'Email Address',

            'phone_number': 'Phone Number',

            'address1': 'Address Line 1',

            'address2': 'Address Line 2',

            'city': 'City',

            'county': 'County',

            'country': 'Country',

            'postal_code': 'Postal Code',
        }

        self.fields['full_name'].widget.atrrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.atrrs['placeholder'] = placeholder
            self.fields[field].label = False
