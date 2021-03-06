# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0011_delete_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to='awardsapp.Image'),
        ),
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='awardsapp.Project'),
        ),
    ]
