# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizXZ', '0003_auto_20160302_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userchoice',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='userchoice',
            name='user',
        ),
        migrations.AddField(
            model_name='choice',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='userChoice',
        ),
    ]
