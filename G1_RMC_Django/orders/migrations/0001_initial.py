# Generated by Django 5.0.1 on 2024-03-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('oid', models.AutoField(primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=200)),
                ('contactno', models.IntegerField()),
                ('grade', models.CharField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('totalbatch', models.IntegerField(default=0)),
            ],
        ),
    ]
