# Generated by Django 3.2.8 on 2021-10-31 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20211031_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='our_address',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='our_address',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
