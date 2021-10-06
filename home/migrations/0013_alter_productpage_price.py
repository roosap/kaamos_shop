# Generated by Django 3.2.5 on 2021-10-06 00:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211006_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='price',
            field=models.IntegerField(default=10000, validators=[django.core.validators.MinValueValidator(500)]),
        ),
    ]
