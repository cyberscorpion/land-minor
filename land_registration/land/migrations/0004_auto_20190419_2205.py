# Generated by Django 2.1.7 on 2019-04-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0003_auto_20190418_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidland',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bidland',
            name='itter',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bidland',
            name='sell_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bidland',
            name='selling_value',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]