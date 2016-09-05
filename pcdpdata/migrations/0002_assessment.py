# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcdpdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('original_id', models.IntegerField()),
                ('type', models.IntegerField()),
                ('project', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, to='pcdpdata.Project', null=True)),
            ],
        ),
    ]
