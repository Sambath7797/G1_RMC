# Generated by Django 5.0.1 on 2024-03-08 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('clientname', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('value', models.IntegerField()),
                ('pending', models.IntegerField()),
            ],
        ),
    ]
