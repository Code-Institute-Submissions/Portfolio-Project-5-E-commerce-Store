# Generated by Django 3.2 on 2023-04-12 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_management', '0003_contact_newsletter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-sent_on']},
        ),
    ]
