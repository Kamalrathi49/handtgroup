# Generated by Django 3.2.8 on 2021-10-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='our_address',
            old_name='Address',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='our_address',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='our_address',
            name='pin_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='our_address',
            name='telephone',
            field=models.IntegerField(),
        ),
    ]
