# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0009_auto_20150903_0154'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_auto_20151022_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemInCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('size', models.CharField(max_length=25)),
                ('product_name', models.ForeignKey(to='clothing.ApparelInfo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderticket',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='orderticket',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderTicket',
        ),
    ]
