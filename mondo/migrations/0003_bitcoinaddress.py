# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mondo', '0002_auto_20160123_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=40)),
                ('account', models.ForeignKey(to='mondo.MondoAccount')),
            ],
        ),
    ]
