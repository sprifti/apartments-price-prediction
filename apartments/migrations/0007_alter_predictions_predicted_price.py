# Generated by Django 3.2.5 on 2021-07-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0006_alter_apartment_interior_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='predicted_price',
            field=models.DecimalField(decimal_places=20, max_digits=40),
        ),
    ]
