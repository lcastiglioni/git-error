# Generated by Django 4.1 on 2022-08-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0005_alter_bakeries_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=1942),
        ),
    ]
