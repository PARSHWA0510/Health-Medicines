# Generated by Django 2.2.1 on 2022-07-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_cart_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='tot_price',
            field=models.CharField(default='0', max_length=5),
        ),
    ]
