# Generated by Django 3.1.1 on 2020-10-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockQuotes', '0016_auto_20201012_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='buystockmodel',
            name='account',
            field=models.DecimalField(decimal_places=0, default=30000, max_digits=15),
        ),
        migrations.AlterField(
            model_name='buystockmodel',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
        migrations.AlterField(
            model_name='buystockmodel',
            name='total_value',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=15),
        ),
    ]