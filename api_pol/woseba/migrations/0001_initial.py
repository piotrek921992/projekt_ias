# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(default='', max_length=200)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('ilosc', models.IntegerField(default=0)),
            ],
        ),
    ]