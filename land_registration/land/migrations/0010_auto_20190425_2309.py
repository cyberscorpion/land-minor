# Generated by Django 2.1.7 on 2019-04-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0009_auto_20190425_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='itter',
            field=models.PositiveIntegerField(default=1),
        ),
    ]