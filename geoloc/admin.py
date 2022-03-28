from django.contrib import admin
from .models import Location, Language, TimeZone, Currency, Connection, GeoLocalization


admin.site.register(Location)
admin.site.register(Language)
admin.site.register(TimeZone)
admin.site.register(Currency)
admin.site.register(Connection)
admin.site.register(GeoLocalization)
