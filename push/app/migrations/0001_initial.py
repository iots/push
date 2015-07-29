# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PushModel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('push_message', models.CharField(max_length=100, verbose_name='推送消息')),
                ('push_url', models.URLField(verbose_name='推送URL')),
            ],
        ),
    ]
