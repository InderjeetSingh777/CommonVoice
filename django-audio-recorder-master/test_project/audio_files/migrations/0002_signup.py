# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=8)),
                ('college', models.CharField(max_length=50)),
                ('current_location', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('mother_tongue', models.CharField(max_length=50)),
                ('secondary_language', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
