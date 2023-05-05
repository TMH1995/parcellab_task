from rest_framework import serializers
from shipping.models import Shipment
from .article_serializer import ArticleSerializer
from .address_serializer import AddressSerializer

class ShipmentSerializer(serializers.ModelSerializer):

    sender_address= serializers.SerializerMethodField()
    receiver_address= serializers.SerializerMethodField()
    article=serializers.SerializerMethodField()

    def get_sender_address(self,obj:Shipment):
        senderAddressSerializer= AddressSerializer(instance=obj.sender_address)
        return senderAddressSerializer.data
    

    def get_receiver_address(self,obj:Shipment):
        receiverAddressSerializer=  AddressSerializer(instance=obj.receiver_address)
        return receiverAddressSerializer.data
    
    def get_article(self,obj:Shipment):
        articleSerializer= ArticleSerializer(instance=obj.article)
        data= articleSerializer.data
        data['quantity']=obj.article_quantity
        data['price']=obj.article_price
        return data
    

    class Meta:
        model=Shipment
        fields=['tracking_number','carrier','sender_address','receiver_address','article']

