from rest_framework import serializers
from .temperature_serializer import TemperatureSerializer
from shipping.models import Address,Temperature


class AddressSerializer(serializers.ModelSerializer):


    country=serializers.SerializerMethodField()
    city=serializers.SerializerMethodField()
    zipCode=serializers.SerializerMethodField()
    temperature=serializers.SerializerMethodField()

    
    def get_country(self,obj:Address):
        return obj.origin.country

    def get_city(self,obj:Address):
        return obj.origin.city

    def get_zipCode(self,obj:Address):
        return obj.origin.zipCode

    def get_temperature(self,obj:Address):
        termperature=obj.origin.origin_temperature
        temperatureSerializer= TemperatureSerializer(instance=termperature)
        return temperatureSerializer.data
    
    class Meta:
        model = Address
        fields = ['country','city','zipCode','street','temperature']