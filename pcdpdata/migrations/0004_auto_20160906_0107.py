# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcdpdata', '0003_auto_20160906_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True, to='pcdpdata.Project', related_name='assesment'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='pcdpdata.Question', related_name='choices'),
        ),
        migrations.AlterField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(to='pcdpdata.Assessment', related_name='questions'),
        ),
    ]
