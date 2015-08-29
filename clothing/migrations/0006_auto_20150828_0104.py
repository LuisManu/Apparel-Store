# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0005_auto_20150813_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparelinfo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
