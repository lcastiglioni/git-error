# Generated by Django 4.1 on 2022-08-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0026_remove_unic_code_sku_remove_unic_code_unic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=175),
        ),
    ]
