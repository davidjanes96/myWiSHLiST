# Generated by Django 4.0.3 on 2022-08-25 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_wishlist_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlist',
            options={'ordering': ['-modified']},
        ),
    ]
