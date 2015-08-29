# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparelinfo',
            name='image2',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AlterField(
            model_name='apparelinfo',
            name='image3',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AlterField(
            model_name='apparelinfo',
            name='image4',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AlterField(
            model_name='apparelinfo',
            name='image5',
            field=models.ImageField(null=True, upload_to=b'product_images', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='blurb',
            field=models.TextField(),
        ),
    ]
