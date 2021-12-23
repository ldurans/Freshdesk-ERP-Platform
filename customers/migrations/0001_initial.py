# Generated by Django 3.2.9 on 2021-12-23 14:49

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date', models.DateField(verbose_name='Date')),
                ('decsription', models.CharField(max_length=255, verbose_name='Description')),
                ('voucher_no', models.CharField(default='51014488078727', max_length=14, unique=True, verbose_name='Voucher No')),
                ('debit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Debit')),
                ('credit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Credit')),
            ],
            options={
                'verbose_name': 'Ledger',
                'verbose_name_plural': 'Ledgers',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('customer_address', models.CharField(max_length=200)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(default='+8801', max_length=128, region=None)),
                ('city', django_countries.fields.CountryField(default='BD', max_length=2)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('previous_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('customer_ledger', models.ManyToManyField(to='customers.Ledger')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
