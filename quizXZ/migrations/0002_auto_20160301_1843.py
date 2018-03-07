# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizXZ', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('selected', models.BooleanField()),
            ],
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='questionID',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='quizID',
            new_name='quiz',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default=b'', max_length=300),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='quiz',
            name='difficulty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='quiz',
            name='subject',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='choice',
            field=models.ForeignKey(to='quizXZ.Choice'),
        ),
        migrations.AddField(
            model_name='userchoice',
            name='user',
            field=models.ForeignKey(to='quizXZ.User'),
        ),
    ]
