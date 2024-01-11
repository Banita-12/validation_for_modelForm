# Generated by Django 4.2.6 on 2024-01-11 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=10)),
                ('sage', models.IntegerField()),
                ('smobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('[6-9]\\d{9}')])),
            ],
        ),
    ]
