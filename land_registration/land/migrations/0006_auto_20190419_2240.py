# Generated by Django 2.1.7 on 2019-04-19 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0005_auto_20190419_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='land',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
