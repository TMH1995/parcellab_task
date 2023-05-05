from django.test import TestCase,Client
from django.urls import reverse
from shipping.models import Origin,Address,Shipment,Article
import json

class TestTrackTraceView(TestCase):

    def setUp(self) -> None:
        self.origin1= Origin.objects.create(country='Germany',city='Munich',zipCode='81541')
        self.origin2= Origin.objects.create(country='Germany',city='Munich',zipCode='81241')
        self.address1=Address.objects.create(origin=self.origin1,street='Aurbacherstraße')
        self.address2=Address.objects.create(origin=self.origin2,street='Landsberger')
        self.article1=Article.objects.create(name='Laptop',SKU='LP123')
        self.article2=Article.objects.create(name='Phone',SKU='PH456')
        self.shipment1=Shipment.objects.create(tracking_number='TN12345683',carrier='GLS',
                                          sender_address=self.address1,receiver_address=self.address2,
                                          article=self.article1,article_quantity=1,article_price=750)

        self.shipment2=Shipment.objects.create(tracking_number='TN12345684',carrier='DHL',
                                          sender_address=self.address2,receiver_address=self.address1,
                                          article=self.article2,article_quantity=2,article_price=420)
        self.client = Client()
        
    def test_fetch_shipment_details_with_valid_tracking_information(self)->None:
        data={
        "tracking_number": "TN12345683",
        "carrier": "GLS"
        }

        response=self.client.post(reverse('fetchShipmentDetails'),data)
        self.assertEquals(response.status_code,200)
        responseData=json.loads(response.content)['data']
        self.assertEquals(responseData['tracking_number'],"TN12345683")
        self.assertEquals(responseData['carrier'],"GLS")

    def test_fetch_shipment_details_with_invalid_tracking_information(self)->None:
        data={
        "tracking_number": "TN123456877777",
        "carrier": "GLS"
        }

        response=self.client.post(reverse('fetchShipmentDetails'),data)
        self.assertEquals(response.status_code,400)
        responseData=json.loads(response.content)
        self.assertEquals(responseData,{"message": "Wrong tracking number or carrier"})


