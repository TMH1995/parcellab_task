from rest_framework import serializers
from shipping.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['name','SKU']