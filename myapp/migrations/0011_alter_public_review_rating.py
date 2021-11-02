# Generated by Django 3.2.8 on 2021-10-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20211029_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_review',
            name='rating',
            field=models.CharField(choices=[('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE'), ('four', 'FOUR'), ('five', 'FIVE')], default='one', max_length=10),
        ),
    ]
