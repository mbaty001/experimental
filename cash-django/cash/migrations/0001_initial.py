# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('month', models.DecimalField(decimal_places=0, max_digits=2)),
                ('entry_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cash.Person'),
        ),
    ]
