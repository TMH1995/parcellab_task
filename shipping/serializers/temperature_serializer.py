from rest_framework import serializers
from shipping.services import TemperatureService
from shipping.models import Temperature


class TemperatureSerializer(serializers.ModelSerializer):

    degree=serializers.SerializerMethodField()

    def get_degree(self,obj:Temperature):
        if(obj.isMoreThanTwoHours):
            obj.degree=TemperatureService().fetchTemperature(city=obj.origin.city,zipCode=obj.origin.zipCode)
            obj.save()
        return obj.degree

    class Meta:
        model = Temperature
        fields = ['degree']