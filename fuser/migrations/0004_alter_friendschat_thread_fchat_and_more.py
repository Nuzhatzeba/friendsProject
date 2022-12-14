# Generated by Django 4.1.2 on 2022-12-04 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0003_friendschat_thread_threadid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendschat_thread',
            name='fChat',
            field=models.TextField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='friendschat_thread',
            name='fChatTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='friendsuser',
            name='dOB',
            field=models.DateField(null=True),
        ),
    ]
