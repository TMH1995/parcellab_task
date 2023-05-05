from django.db import models
from .origin import Origin

class Address(models.Model):
    origin= models.ForeignKey(Origin,on_delete=models.CASCADE,related_name='origin_streets')
    street= models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.origin} - Street: {self.street}'