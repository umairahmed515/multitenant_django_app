from django.contrib import admin

from hotel_tenant.models import HotelTableReservation


@admin.register(HotelTableReservation)
class HotelTableReservationAdmin(admin.ModelAdmin):
    list_display = ("hotel", "num_of_guests", "num_of_tables", "reserve_table")
