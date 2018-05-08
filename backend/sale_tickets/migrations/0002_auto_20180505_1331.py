# Generated by Django 2.0.4 on 2018-05-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showtimes', '0002_showtime_movie'),
        ('sale_tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketonsale',
            name='auditorium',
        ),
        migrations.RemoveField(
            model_name='ticketonsale',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ticketonsale',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ticketonsale',
            name='price',
        ),
        migrations.RemoveField(
            model_name='ticketonsale',
            name='time',
        ),
        migrations.AddField(
            model_name='ticketonsale',
            name='showtime',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.PROTECT, related_name='tickets_on_sale', to='showtimes.Showtime'),
            preserve_default=False,
        ),
    ]