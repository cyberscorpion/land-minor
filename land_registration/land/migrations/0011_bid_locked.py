# Generated by Django 2.1.7 on 2019-04-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0010_auto_20190425_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
