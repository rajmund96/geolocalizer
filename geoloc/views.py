from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Location, Language, GeoLocalization
from .serializers import LocationSerializer, GeoLocalizationSerializer, TimeZone, Currency, Connection
import requests
import socket


class GeoLocalizationViewSet(ModelViewSet):
    lookup_value_regex = '[^/]+'
    queryset = GeoLocalization.objects.select_related().all()
    serializer_class = GeoLocalizationSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        ip_add = socket.gethostbyname(self.kwargs['pk'])
        instance = GeoLocalization.objects.get(ip=ip_add)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        ip_add = socket.gethostbyname(self.kwargs['pk'])
        queryset = GeoLocalization.objects.select_related().all()
        instance = get_object_or_404(queryset, ip=ip_add)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        with transaction.atomic():
            req_data = request.data
            ip_add = socket.gethostbyname(req_data["ip"])

            response = requests.get(
                f'http://api.ipstack.com/{ip_add}?access_key=ba7bc56947eedf70c8557efd9bb4182b&format=1'
            )
            data = response.json()

            new_loc, _ = Location.objects.get_or_create(geoname_id=data['location']['geoname_id'],
                                                        capital=data['location']['capital'],
                                                        country_flag=data['location']['country_flag'],
                                                        country_flag_emoji=data['location']['country_flag_emoji'],
                                                        country_flag_emoji_unicode=data['location'][
                                                            'country_flag_emoji_unicode'],
                                                        calling_code=data['location']['calling_code'],
                                                        is_eu=data['location']['is_eu'])

            new_loc.save()

            for language in data['location']["languages"]:
                language_obj, _ = Language.objects.get_or_create(code=language['code'], defaults=language)
                new_loc.languages.add(language_obj)

            new_geolocation = GeoLocalization.objects.create(ip=data['ip'],
                                                             type=data['type'],
                                                             continent_code=data['continent_code'],
                                                             continent_name=data['continent_name'],
                                                             country_code=data['country_code'],
                                                             country_name=data['country_name'],
                                                             region_code=data['region_code'],
                                                             region_name=data['region_name'],
                                                             city=data['city'],
                                                             zip=data['zip'],
                                                             latitude=data['latitude'],
                                                             longitude=data['longitude'],
                                                             location=new_loc)
                                                             # time_zone=new_time_zone,
                                                             # currency=new_currency,
                                                             # connection=new_connection)
            new_geolocation.save()

            serializer = GeoLocalizationSerializer(new_geolocation)
            return Response(serializer.data)
