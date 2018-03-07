# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizXZ', '0010_auto_20160419_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='attempt',
            name='user',
        ),
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.DeleteModel(
            name='Attempt',
        ),
    ]
