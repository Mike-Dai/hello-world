# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-29 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20190129_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]