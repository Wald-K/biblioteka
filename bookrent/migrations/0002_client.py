# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookrent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('pesel', models.IntegerField(unique=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
