# Generated by Django 3.2.8 on 2021-10-30 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20211030_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='our_project',
            name='title',
        ),
    ]
