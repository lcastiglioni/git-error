# Generated by Django 4.0.6 on 2022-08-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0024_alter_products_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=166),
        ),
    ]
