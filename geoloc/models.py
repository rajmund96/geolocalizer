from django.db import models


class Language(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    native = models.CharField(max_length=50)


class Location(models.Model):
    geoname_id = models.IntegerField(primary_key=True)
    capital = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)
    country_flag = models.URLField()
    country_flag_emoji = models.CharField(max_length=10)
    country_flag_emoji_unicode = models.CharField(max_length=200)
    calling_code = models.CharField(max_length=10)
    is_eu = models.BooleanField()


class TimeZone(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    current_time = models.CharField(max_length=200)
    gmt_offset = models.IntegerField()
    code = models.CharField(max_length=200)
    is_daylight_saving = models.BooleanField()


class Currency(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=200)
    plural = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    symbol_native = models.CharField(max_length=10)


class Connection(models.Model):
    asn = models.PositiveIntegerField(primary_key=True)
    isp = models.CharField(max_length=200)


class GeoLocalization(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    type = models.CharField(max_length=4)
    continent_code = models.CharField(max_length=10)
    continent_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=4)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=4)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    # time_zone = models.ForeignKey(TimeZone, on_delete=models.PROTECT)
    # currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    # connection = models.ForeignKey(Connection, on_delete=models.PROTECT)



