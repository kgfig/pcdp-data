# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pcdpdata', '0004_auto_20160906_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='project',
            field=models.ForeignKey(null=True, blank=True, related_name='assesment_list', on_delete=django.db.models.deletion.SET_NULL, to='pcdpdata.Project'),
        ),
    ]
