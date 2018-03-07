# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizXZ', '0011_auto_20160420_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz', models.ForeignKey(to='quizXZ.Quiz')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='quizXZ.QuizUser', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='quizuser',
            unique_together=set([('user', 'quiz')]),
        ),
    ]
