# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('depart', models.DateTimeField()),
                ('arrivee', models.DateTimeField()),
                ('origine', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('modele', models.CharField(max_length=10)),
            ],
        ),
    ]
