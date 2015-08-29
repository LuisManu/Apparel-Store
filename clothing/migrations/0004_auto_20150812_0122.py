# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0003_auto_20150811_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApparelImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='apparelinfo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='apparelinfo',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='apparelinfo',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='apparelinfo',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='apparelinfo',
            name='image5',
        ),
        migrations.AddField(
            model_name='apparelimage',
            name='property',
            field=models.ForeignKey(related_name='images', to='clothing.ApparelInfo'),
        ),
    ]
