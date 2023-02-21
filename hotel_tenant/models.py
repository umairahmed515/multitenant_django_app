from django.db import models

from hotel_shared.models import Hotel


class HotelTableReservation(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    num_of_guests = models.IntegerField(default=0)
    num_of_tables = models.IntegerField()
    reserve_table = models.BooleanField(default=False)
