# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-20 08:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0005_auto_20171019_0848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
            ],
            options={
                'db_table': 'Comment',
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(default=b'2017-10-20 08:08:11', verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='comment',
            name='articles',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_article', to='article.article', verbose_name='\u8bc4\u8bba\u6587\u7ae0'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='\u8bc4\u8bba\u7528\u6237'),
        ),
    ]
