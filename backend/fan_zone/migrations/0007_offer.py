# Generated by Django 2.0.5 on 2018-05-22 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fan_zone', '0006_auto_20180515_0619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='fan_zone.Prop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prop_offers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]