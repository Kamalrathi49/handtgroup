# Generated by Django 3.2.8 on 2021-10-29 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_our_service_is_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='our_projects',
            new_name='our_project',
        ),
        migrations.AlterField(
            model_name='our_service',
            name='is_active',
            field=models.CharField(choices=[('true', 'TRUE'), ('false', 'FALSE')], default='true', max_length=6),
        ),
    ]
