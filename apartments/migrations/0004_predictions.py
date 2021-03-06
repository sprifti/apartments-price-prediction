# Generated by Django 3.2.5 on 2021-07-11 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0003_delete_predictions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_price', models.DecimalField(decimal_places=5, max_digits=5)),
                ('accurate', models.BooleanField(null=True)),
                ('apartment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='apartments.apartment')),
            ],
        ),
    ]
