# Generated by Django 3.2 on 2023-04-08 12:38

from django.db import migrations
import products.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=products.fields.CaseInsensitiveCharField(max_length=254, unique=True),
        ),
    ]
