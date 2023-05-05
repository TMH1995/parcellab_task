from django.db import models


class Article(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    SKU=models.CharField(max_length=10,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name} - SKU: {self.SKU}'