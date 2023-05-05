from django.db import models


class Origin(models.Model):
    country= models.CharField(max_length=50,null=False,blank=False)
    city= models.CharField(max_length=50,null=False,blank=False)
    zipCode=models.CharField(max_length=10,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Country: {self.country} - City: {self.city} - Zip Code: {self.zipCode}'