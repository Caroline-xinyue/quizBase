# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0008_auto_20160419_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selection',
            name='attempt',
        ),
        migrations.RemoveField(
            model_name='selection',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='userattempt',
            name='users',
        ),
        migrations.DeleteModel(
            name='Selection',
        ),
        migrations.DeleteModel(
            name='UserAttempt',
        ),
    ]
