# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mondo', '0003_bitcoinaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitcoinaddress',
            name='last_balance',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
