# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_info', '0002_auto_20170325_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_image',
        ),
    ]
