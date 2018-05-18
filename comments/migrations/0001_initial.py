# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-30 07:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Study', '0005_auto_20180430_1503'),
        ('life', '0004_auto_20180430_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='LComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('text', models.TextField()),
                ('created_time', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='life.LPost')),
            ],
        ),
        migrations.CreateModel(
            name='SComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('text', models.TextField()),
                ('created_time', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Study.SPost')),
            ],
        ),
    ]