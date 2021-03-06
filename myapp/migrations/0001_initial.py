# Generated by Django 3.2.8 on 2021-10-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='our_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=15)),
                ('telephone', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='our_partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='partner_logo/')),
            ],
        ),
        migrations.CreateModel(
            name='our_projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='our_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='icons/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=700)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(choices=[('true', 'TRUE'), ('false', 'FALSE')], default=True, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='planning_stag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=700)),
                ('image', models.FileField(upload_to='property_images/')),
            ],
        ),
        migrations.CreateModel(
            name='public_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=700)),
                ('icon', models.FileField(upload_to='profile_pic/')),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
    ]
