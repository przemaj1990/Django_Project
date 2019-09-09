# Generated by Django 2.2.5 on 2019-09-09 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Workshop_RoomsMgt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rooms', to='Workshop_RoomsMgt.Room', verbose_name='Rooms'),
        ),
    ]
