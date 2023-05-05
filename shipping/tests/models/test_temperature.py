from django.test import TestCase
from shipping.models import Origin,Temperature

class TestTemperature(TestCase):

    def setUp(self) -> None:
        self.origin1= Origin.objects.create(country='Germany',city='Munich',zipCode='81541')
        self.origin2= Origin.objects.create(country='Germany',city='Munich',zipCode='81241')

    def test_address_creation(self)->None:
        temperature1=Temperature.objects.get(origin=self.origin1)
        temperature1.degree=18.2
        temperature1.save()

        temperature2=Temperature.objects.get(origin=self.origin2)
        temperature2.degree=-2.5
        temperature2.save()
        
        self.assertEquals(temperature1.degree,18.2)
        self.assertEquals(temperature1.origin.country,'Germany')
        self.assertEquals(temperature1.origin.city,'Munich')
        self.assertEquals(temperature1.origin.zipCode,'81541')

        self.assertEquals(temperature2.degree,-2.5)
        self.assertEquals(temperature2.origin.country,'Germany')
        self.assertEquals(temperature2.origin.city,'Munich')
        self.assertEquals(temperature2.origin.zipCode,'81241')
