# Generated by Django 3.2.9 on 2021-12-23 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('service_name', models.CharField(max_length=100)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('vat', models.DecimalField(blank=True, decimal_places=2, default=2.0, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
