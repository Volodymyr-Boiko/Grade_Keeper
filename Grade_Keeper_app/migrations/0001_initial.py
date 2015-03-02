# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('assigment_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
                ('text', models.CharField(max_length=1000)),
                ('due_date', models.DateField()),
                ('points_possible', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=40)),
                ('e_mail', models.EmailField(max_length=30)),
                ('point', models.IntegerField(default=0)),
                ('assignments', models.ForeignKey(to='Grade_Keeper_app.Assignments')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
