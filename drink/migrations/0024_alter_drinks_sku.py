# Generated by Django 4.0.6 on 2022-08-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drink', '0023_alter_drinks_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='sku',
            field=models.IntegerField(default=851),
        ),
    ]