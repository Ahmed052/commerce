# Generated by Django 4.2.4 on 2023-09-21 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_auction_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='auction',
            name='category',
        ),
    ]
