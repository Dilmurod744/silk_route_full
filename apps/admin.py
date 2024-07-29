from django.contrib import admin

from apps.models import Packages, Contacts, Booking


# Register your models here.
@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
