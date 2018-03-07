# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0012_auto_20160420_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='subject',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
