from django.test import TestCase
from shipping.models import Origin


class TestOrigin(TestCase):

    def test_article_creation(self)->None:
        origin1= Origin.objects.create(country='Germany',city='Munich',zipCode='81541')
        origin2= Origin.objects.create(country='Germany',city='Munich',zipCode='81241')

        self.assertEquals(origin1.country,'Germany')
        self.assertEquals(origin1.city,'Munich')
        self.assertEquals(origin1.zipCode,'81541')

        self.assertEquals(origin2.country,'Germany')
        self.assertEquals(origin2.city,'Munich')
        self.assertEquals(origin2.zipCode,'81241')
