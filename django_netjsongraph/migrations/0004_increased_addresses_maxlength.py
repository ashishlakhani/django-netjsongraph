# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_netjsongraph', '0003_topology_receive_strategy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='addresses',
            field=models.CharField(db_index=True, max_length=510),
        )
    ]