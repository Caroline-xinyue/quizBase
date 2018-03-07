# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0013_auto_20160420_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='difficulty',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
    ]
