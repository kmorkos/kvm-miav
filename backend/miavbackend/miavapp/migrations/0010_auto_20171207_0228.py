# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 07:28
from __future__ import unicode_literals

from django.db import migrations, models
import miavapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('miavapp', '0009_auto_20171206_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(max_length=20, validators=[miavapp.validators.validate_status]),
        ),
    ]
