# Generated by Django 4.2.11 on 2024-04-03 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='tenant',
        ),
        migrations.AddField(
            model_name='tenant',
            name='team',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='customers.teams'),
            preserve_default=False,
        ),
    ]
