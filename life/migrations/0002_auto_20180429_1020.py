# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-29 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lpost',
            name='img',
            field=models.ImageField(upload_to='SImg', verbose_name='\u914d\u56fe'),
        ),
    ]
