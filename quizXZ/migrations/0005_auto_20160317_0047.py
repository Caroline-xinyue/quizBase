# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0004_auto_20160303_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='point',
            field=models.IntegerField(default=0, choices=[(0, 0), (1, 0.5), (2, 1)]),
        ),
    ]
