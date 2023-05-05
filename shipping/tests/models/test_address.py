from django.test import TestCase
from shipping.models import Origin,Address

class TestAddress(TestCase):

    def setUp(self) -> None:
        self.origin1= Origin.objects.create(country='Germany',city='Munich',zipCode='81541')
        self.origin2= Origin.objects.create(country='Germany',city='Munich',zipCode='81241')

    def test_address_creation(self)->None:
        address1=Address.objects.create(origin=self.origin1,street='Aurbacherstraße')
        address2=Address.objects.create(origin=self.origin2,street='Landsberger')
        
        self.assertEquals(address1.street,'Aurbacherstraße')
        self.assertEquals(address1.origin.country,'Germany')
        self.assertEquals(address1.origin.city,'Munich')
        self.assertEquals(address1.origin.zipCode,'81541')

        self.assertEquals(address2.street,'Landsberger')
        self.assertEquals(address2.origin.country,'Germany')
        self.assertEquals(address2.origin.city,'Munich')
        self.assertEquals(address2.origin.zipCode,'81241')
