# Generated by Django 2.0.4 on 2018-04-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theaters', '0005_merge_20180427_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]