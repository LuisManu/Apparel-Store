# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0004_auto_20150812_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apparelimage',
            name='property',
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='image',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='image2',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='image3',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='image4',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='image5',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.DeleteModel(
            name='ApparelImage',
        ),
    ]
