# Generated by Django 4.2.4 on 2023-09-17 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_auction_starting_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
    ]
