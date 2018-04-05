# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-02 06:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podrequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='firmware',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x0_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x1_gateway',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x1_subnetmask',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x3_gateway',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x3_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='x3_subnetmask',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
