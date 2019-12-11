# Generated by Django 3.0 on 2019-12-07 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191207_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='add_on_accessory',
        ),
        migrations.RemoveField(
            model_name='car',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='car',
            name='pickup_date',
        ),
        migrations.RemoveField(
            model_name='car',
            name='return_date',
        ),
        migrations.RemoveField(
            model_name='car',
            name='total_price',
        ),
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateTimeField(blank=True, null=True, verbose_name='pick_up_time')),
                ('return_date', models.DateTimeField(blank=True, null=True, verbose_name='return_time')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='app.Car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'car',
            },
        ),
    ]
