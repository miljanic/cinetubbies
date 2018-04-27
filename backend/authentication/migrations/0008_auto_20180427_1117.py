# Generated by Django 2.0.4 on 2018-04-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_theateradmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('theater-admin', 'Theater Admin'), ('fan-zone-admin', 'Fan Zone Admin'), ('user', 'User')], default='user', max_length=20),
        ),
    ]