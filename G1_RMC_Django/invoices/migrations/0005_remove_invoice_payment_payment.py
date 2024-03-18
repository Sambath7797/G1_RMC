# Generated by Django 5.0.1 on 2024-03-15 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0004_rename_total_value_invoice_gross_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payment',
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('payment_amt', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='invoices.invoice')),
            ],
        ),
    ]