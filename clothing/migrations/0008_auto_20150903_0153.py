# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='apparelinfo',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='likes',
            field=models.ManyToManyField(to='clothing.ApparelInfo', blank=True),
        ),
    ]
