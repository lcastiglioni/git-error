# Generated by Django 4.1 on 2022-08-20 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meat', '0004_alter_products_sku'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Meats'},
        ),
        migrations.AlterField(
            model_name='products',
            name='sku',
            field=models.IntegerField(default=1856),
        ),
    ]