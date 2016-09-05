# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcdpdata', '0002_assessment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField()),
                ('original_id', models.IntegerField()),
                ('letter', models.CharField(max_length=1)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField()),
                ('original_id', models.IntegerField()),
                ('seq_num', models.IntegerField()),
                ('points', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstname', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('original_id', models.IntegerField()),
                ('answers', models.ManyToManyField(to='pcdpdata.Choice')),
            ],
        ),
        migrations.AlterField(
            model_name='assessment',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AddField(
            model_name='question',
            name='assessment',
            field=models.ForeignKey(to='pcdpdata.Assessment'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='pcdpdata.Question'),
        ),
    ]
