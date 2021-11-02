# Generated by Django 3.2.8 on 2021-10-31 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_rename_project_name_our_project_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='top_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=99)),
                ('security_image', models.ImageField(upload_to='top-image/')),
                ('construction_image', models.ImageField(upload_to='top-image/')),
                ('manpower_image', models.ImageField(upload_to='top-image/')),
                ('realestate_image', models.ImageField(upload_to='top-image/')),
                ('is_active', models.CharField(choices=[('true', 'TRUE'), ('false', 'FALSE')], default='true', max_length=6)),
            ],
        ),
    ]
