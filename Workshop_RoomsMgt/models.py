from django.db import models
import datetime


class Room(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=64
    )
    capacity = models.SmallIntegerField(
        verbose_name='Capacity'
    )
    projector_availability = models.BooleanField(
        verbose_name='Projector availability',
        default=True
    )

    def __str__(self):
        return self.name

    def today_check(self):
        today = datetime.date.today()
        today_res = []
        r = self.Rooms.all()
        for d in r:
            today_res.append(d.date)
        if today in today_res:
            return True
        else:
            return False


class Reservation(models.Model):
    date = models.DateField(
        verbose_name='Date',
    )
    comment = models.CharField(
        verbose_name='Comment',
        max_length=128
    )
    rooms = models.ForeignKey(
        Room,
        verbose_name="Rooms",
        on_delete=models.CASCADE,
        related_name='Rooms'
    )
