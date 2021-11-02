# Generated by Django 3.2.8 on 2021-10-30 10:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_alter_our_service_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='our_team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('role', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='our_project',
            name='project_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]