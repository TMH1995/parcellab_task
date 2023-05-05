import csv
from shipping.services import AddressImportService,ArticleImportService
from shipping.models import Shipment
path='shipments.csv'

# TN12345678,DHL,"Street 1, 10115 Berlin, Germany","Street 10, 75001 Paris, France",Laptop,1,800,LP123
class Seeder:
    def __init__(self):
        self.addressImportService= AddressImportService()
        self.articleImportService=ArticleImportService()
    def seed(self):
        with open(path) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                [tracking_number,carrier,sender_address,receiver_address,article_name,article_quantity,article_price,sku]=row
                article=self.articleImportService.handleArticleFetch(name=article_name,SKU=sku)
                sender_address_object=self.addressImportService.handleAddressFetch(sender_address)
                receiver_address_object=self.addressImportService.handleAddressFetch(receiver_address)
                try:
                    Shipment.objects.create(tracking_number=tracking_number,carrier=carrier,sender_address=sender_address_object,
                    receiver_address=receiver_address_object,article=article,article_quantity=article_quantity,article_price=article_price)
                except Exception as e:
                    print(e)

if(__name__ == '__main__'):
    Seeder().seed()