# Generated by Django 4.2.4 on 2023-09-20 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_category_auction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='winner',
        ),
        migrations.AlterField(
            model_name='auction',
            name='date_of_auction',
            field=models.DateField(default=datetime.date(2023, 9, 20), null=True),
        ),
    ]