# Generated by Django 4.2.1 on 2023-08-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreact', '0002_eurusd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eurusd',
            name='timestamp',
            field=models.DecimalField(decimal_places=12, max_digits=13),
        ),
    ]
