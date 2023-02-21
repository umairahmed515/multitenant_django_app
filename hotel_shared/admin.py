from django.contrib import admin

from hotel_shared.models import Hotel


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("hotel_name", "hotel_type")
