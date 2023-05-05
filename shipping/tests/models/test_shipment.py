from django.test import TestCase
from shipping.models import Origin,Address,Shipment,Article

class TestShipment(TestCase):

    def setUp(self) -> None:
        self.origin1= Origin.objects.create(country='Germany',city='Munich',zipCode='81541')
        self.origin2= Origin.objects.create(country='Germany',city='Munich',zipCode='81241')
        self.address1=Address.objects.create(origin=self.origin1,street='Aurbacherstraße')
        self.address2=Address.objects.create(origin=self.origin2,street='Landsberger')
        self.article1=Article.objects.create(name='Laptop',SKU='LP123')
        self.article2=Article.objects.create(name='Phone',SKU='PH456')

    def test_address_creation(self)->None:
        shipment1=Shipment.objects.create(tracking_number='TN12345683',carrier='GLS',
                                          sender_address=self.address1,receiver_address=self.address2,
                                          article=self.article1,article_quantity=1,article_price=750)

        shipment2=Shipment.objects.create(tracking_number='TN12345684',carrier='DHL',
                                          sender_address=self.address2,receiver_address=self.address1,
                                          article=self.article2,article_quantity=2,article_price=420)
        
        self.assertEquals(shipment1.tracking_number,'TN12345683')
        self.assertEquals(shipment1.carrier,'GLS')
        self.assertEquals(shipment1.sender_address.street,'Aurbacherstraße')
        self.assertEquals(shipment1.sender_address.origin.country,'Germany')
        self.assertEquals(shipment1.sender_address.origin.city,'Munich')
        self.assertEquals(shipment1.sender_address.origin.zipCode,'81541')
        self.assertEquals(shipment1.receiver_address.street,'Landsberger')
        self.assertEquals(shipment1.receiver_address.origin.country,'Germany')
        self.assertEquals(shipment1.receiver_address.origin.city,'Munich')
        self.assertEquals(shipment1.receiver_address.origin.zipCode,'81241')
        self.assertEquals(shipment1.article.name,'Laptop')
        self.assertEquals(shipment1.article.SKU,'LP123')
        self.assertEquals(shipment1.article_quantity,1)
        self.assertEquals(shipment1.article_price,750)


        self.assertEquals(shipment2.tracking_number,'TN12345684')
        self.assertEquals(shipment2.carrier,'DHL')
        self.assertEquals(shipment2.sender_address.street,'Landsberger')
        self.assertEquals(shipment2.sender_address.origin.country,'Germany')
        self.assertEquals(shipment2.sender_address.origin.city,'Munich')
        self.assertEquals(shipment2.sender_address.origin.zipCode,'81241')
        self.assertEquals(shipment2.receiver_address.street,'Aurbacherstraße')
        self.assertEquals(shipment2.receiver_address.origin.country,'Germany')
        self.assertEquals(shipment2.receiver_address.origin.city,'Munich')
        self.assertEquals(shipment2.receiver_address.origin.zipCode,'81541')
        self.assertEquals(shipment2.article.name,'Phone')
        self.assertEquals(shipment2.article.SKU,'PH456')
        self.assertEquals(shipment2.article_quantity,2)
        self.assertEquals(shipment2.article_price,420)