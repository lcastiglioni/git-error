# Generated by Django 4.0.6 on 2022-08-29 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0024_alter_bakeries_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField(default=1133)),
            ],
        ),
        migrations.CreateModel(
            name='Unic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unic', models.CharField(default='b', max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bakeries',
            options={},
        ),
        migrations.AlterField(
            model_name='bakeries',
            name='sku',
            field=models.IntegerField(default=616),
        ),
        migrations.CreateModel(
            name='Unic_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='bakery.sku')),
                ('unic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='bakery.unic')),
            ],
            options={
                'verbose_name_plural': 'Bakeries',
            },
        ),
    ]
