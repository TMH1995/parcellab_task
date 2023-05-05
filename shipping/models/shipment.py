from django.db import models
from .article import Article
from .address import Address

class Shipment(models.Model):
    tracking_number= models.CharField(max_length=20,null=False,blank=False)
    carrier=models.CharField(max_length=20,null=False,blank=False)
    sender_address= models.ForeignKey(Address,null=True,blank=False,on_delete=models.SET_NULL,related_name='sender_shipments')
    receiver_address= models.ForeignKey(Address,null=True,blank=False,on_delete=models.SET_NULL,related_name='receiver_shipments')
    article= models.ForeignKey(Article,null=True,blank=False,on_delete=models.SET_NULL,related_name='article_shipments')
    article_quantity= models.IntegerField(null=False,blank=False)
    article_price= models.FloatField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('tracking_number', 'carrier',)

    def __str__(self):
        return f'Carrier: {self.carrier} - Tracking Number: {self.tracking_number}'
