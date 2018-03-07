# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0016_auto_20160422_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.IntegerField(default=0, blank=True, choices=[(0, b'easy'), (1, b'medium'), (2, b'hard')]),
        ),
    ]
