# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20171019_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='collect',
            name='has_collect',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u6536\u85cf'),
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(default=b'2017-10-19 08:08:20', verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
