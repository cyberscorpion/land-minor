# Generated by Django 2.1.7 on 2019-04-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0007_auto_20190425_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='days',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='bid',
            name='token_money',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
