# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReviewManager',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='ratings',
            new_name='rating',
        ),
    ]
