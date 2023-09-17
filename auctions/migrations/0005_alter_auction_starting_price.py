# Generated by Django 4.2.4 on 2023-09-17 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auction_date_of_auction_comment_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='starting_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='starting_price', to='auctions.bid'),
        ),
    ]