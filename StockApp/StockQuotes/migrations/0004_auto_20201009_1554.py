# Generated by Django 3.1.1 on 2020-10-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockQuotes', '0003_auto_20201009_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='init_amount',
            name='bank',
            field=models.DecimalField(decimal_places=2, default=10000.0, editable='True', max_digits=8),
        ),
    ]
