from rest_framework import serializers
from .models import Location, Language, TimeZone, Currency, Connection, GeoLocalization


class GeoLocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoLocalization
        fields = '__all__'
        depth = 2


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        depth = 1
