# Generated by Django 3.2.5 on 2021-07-14 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0008_rename_accurate_predictions_accurate_prices'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predictions',
            old_name='accurate_prices',
            new_name='accurate_price',
        ),
    ]