# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_review_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='poster_src',
            field=models.ImageField(blank=True, default='', upload_to='items_poster/'),
        ),
    ]