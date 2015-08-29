# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApparelInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('xsmall', models.IntegerField(default=0)),
                ('small', models.IntegerField(default=0)),
                ('medium', models.IntegerField(default=0)),
                ('large', models.IntegerField(default=0)),
                ('xlarge', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to=b'product_images')),
                ('image2', models.ImageField(upload_to=b'product_images')),
                ('image3', models.ImageField(upload_to=b'product_images')),
                ('image4', models.ImageField(upload_to=b'product_images')),
                ('image5', models.ImageField(upload_to=b'product_images')),
            ],
            options={
                'verbose_name': 'Apparel Item',
            },
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'carousel_images')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=6)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('blurb', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('hours', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'store_images')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='category',
            field=models.ForeignKey(to='clothing.Category'),
        ),
        migrations.AddField(
            model_name='apparelinfo',
            name='department',
            field=models.ForeignKey(to='clothing.Department'),
        ),
    ]
