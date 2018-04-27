# Generated by Django 2.0.4 on 2018-04-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_user_first_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_login',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('cinema_admin', 'Cinema Admin'), ('fan_zone_admin', 'FanZone Admin'), ('user', 'User'), ('user', 'User')], default='user', max_length=20),
        ),
    ]