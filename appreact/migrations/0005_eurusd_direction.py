# Generated by Django 4.2.1 on 2023-08-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appreact', '0004_alter_eurusd_close_alter_eurusd_high_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eurusd',
            name='direction',
            field=models.BooleanField(default=True),
        ),
    ]
