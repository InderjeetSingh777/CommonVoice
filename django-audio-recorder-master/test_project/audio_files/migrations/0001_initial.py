# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('audio_file', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=50)),
                ('yesCount', models.IntegerField()),
                ('noCount', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
            ],
        ),
    ]
