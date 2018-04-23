# Generated by Django 2.0.4 on 2018-04-23 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_remove_movie_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='admin',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]