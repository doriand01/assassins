# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-06 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assassinapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameobject',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameobject',
            name='is_idle',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='gameobject',
            name='lobby',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='assassinapp.LobbyObject'),
        ),
        migrations.AddField(
            model_name='lobbyobject',
            name='creation_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 17, 32, 1, 948342, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='lobbyobject',
            name='expiration_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 19, 32, 1, 948379, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='lobbyobject',
            name='key',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='lobbyobject',
            name='lobby_uuid',
            field=models.CharField(default=b'279dd15b-47d8-406e-9d3f-c66732bf769b', max_length=36),
        ),
        migrations.AlterField(
            model_name='playerobject',
            name='creation_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 6, 17, 32, 1, 947604, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='playerobject',
            name='expiration_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 7, 17, 32, 1, 947643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='playerobject',
            name='player_uuid',
            field=models.CharField(default=b'298ce6a5-eac6-4265-a995-2d0dba441e70', max_length=36),
        ),
    ]
