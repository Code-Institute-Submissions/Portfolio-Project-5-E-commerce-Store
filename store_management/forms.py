from django import forms

from .models import Comment, Newsletter, Contact

from products.models import Product, Category


class ProductForm(forms.ModelForm):

    # This first line of Code (name) is from Javed [Stack over flow]
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off', 'pattern':'^[A-Za-z0-9 ]+$', 'title':'This field can only contain numbers and letters. '}))

    class Meta:

        model = Product

        fields = '__all__'

        exclude = ('date', 'slug', )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'name': 'Name',

            'model_name': 'Model Name',

            'category': 'Category',

            'description': 'Description',

            'size': 'Size',

            'image': 'Image',

            'price': 'Price',
        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('title', 'user_name', 'content', )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'title': 'Title',

            'user_name': 'Username',

            'content': 'Comment',

        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False


class ApproveCommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = ('title', 'user_name', 'content', 'approved',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'title': 'title',

            'user_name': 'Username',

            'content': 'Comment',

            'approved': 'Approved'

        }

        for field in self.fields:

            self.fields[field].widget.attrs = {'readonly':'readonly'}

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False
            
            self.fields['approved'].label = 'Approve comment'


class NewsletterForm(forms.ModelForm):

    class Meta:

        model = Newsletter

        fields = '__all__'

        exclude = ('date',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'email': 'Email',

        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False




class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = '__all__'
        exclude = ('sent_on', 'user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {

            'name': 'Name',
            'email_address': 'Email',
            'tel_number': 'Tel No.',
            'message': 'Message',

        }

        for field in self.fields:

            placeholder = placeholders[field]

            self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].label = False
