# Generated by Django 4.2.11 on 2024-04-02 02:51

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_tenant_teams'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True, verbose_name='Country'),
        ),
    ]