# Generated by Django 2.0.6 on 2019-05-04 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0018_booking_details_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking_details',
            name='return_date',
        ),
    ]
