# Generated by Django 2.0.6 on 2019-04-17 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0008_auto_20190416_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysiteuser',
            name='user_token',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
