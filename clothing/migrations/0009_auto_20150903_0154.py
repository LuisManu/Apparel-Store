# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0008_auto_20150903_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apparelinfo',
            old_name='likes',
            new_name='likes_counter',
        ),
    ]
