# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-28 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
    ]
