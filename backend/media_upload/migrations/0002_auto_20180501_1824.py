# Generated by Django 2.0.4 on 2018-05-01 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]