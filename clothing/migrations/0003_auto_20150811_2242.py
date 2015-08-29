# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0002_auto_20150811_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
