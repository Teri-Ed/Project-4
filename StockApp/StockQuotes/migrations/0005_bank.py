# Generated by Django 3.1.1 on 2020-10-10 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockQuotes', '0004_auto_20201009_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.CharField(max_length=10)),
            ],
        ),
    ]
