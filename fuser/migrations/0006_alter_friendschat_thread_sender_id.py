# Generated by Django 4.1.2 on 2022-12-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuser', '0005_alter_friendswith_a_uid_alter_friendswith_b_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendschat_thread',
            name='sender_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fuser.friendsuser'),
        ),
    ]
