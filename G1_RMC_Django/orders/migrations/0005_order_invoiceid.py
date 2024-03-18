# Generated by Django 5.0.1 on 2024-03-15 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
        ('orders', '0004_rename_price_order_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoiceid',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice'),
            preserve_default=False,
        ),
    ]