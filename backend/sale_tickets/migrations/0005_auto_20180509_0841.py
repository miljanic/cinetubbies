# Generated by Django 2.0.5 on 2018-05-09 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sale_tickets', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='showtime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='showtimes.Showtime'),
        ),
    ]