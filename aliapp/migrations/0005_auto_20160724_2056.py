# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-24 20:56
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('aliapp', '0004_userapps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserApps',
            new_name='UserApp',
        ),
        migrations.AlterModelManagers(
            name='app',
            managers=[
                ('apps', django.db.models.manager.Manager()),
            ],
        ),
    ]