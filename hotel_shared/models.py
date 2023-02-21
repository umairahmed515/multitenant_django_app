from django.db import models

from hotel_shared.enums import HotelTypes

HOTEL_TYPE_CHOICES = (
    (HotelTypes.ONE_STAR.name, HotelTypes.ONE_STAR.value),
    (HotelTypes.TWO_STAR.name, HotelTypes.TWO_STAR.value),
    (HotelTypes.THREE_STAR.name, HotelTypes.THREE_STAR.value),
    (HotelTypes.FOUR_STAR.name, HotelTypes.FOUR_STAR.value),
    (HotelTypes.FIVE_STAR.name, HotelTypes.FIVE_STAR.value),
    (HotelTypes.LUXURY.name, HotelTypes.LUXURY.value),
    (HotelTypes.BUDGET.name, HotelTypes.BUDGET.value),
)


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_type = models.CharField(
        max_length=50,
        choices=HOTEL_TYPE_CHOICES,
        default=HotelTypes.THREE_STAR.value,
        unique=True,
    )

    def __str__(self):
        return f"{self.hotel_name}-{self.hotel_type}"
