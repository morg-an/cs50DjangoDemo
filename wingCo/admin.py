from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.

# this is a way to configure the admin panel
# specifically necessary to 
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Flight)
admin.site.register(Airport)
admin.site.register(Passenger, PassengerAdmin)