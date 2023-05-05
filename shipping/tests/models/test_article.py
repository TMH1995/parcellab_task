from django.test import TestCase
from shipping.models import Article


class TestArticle(TestCase):

    def test_article_creation(self)->None:
        article1=Article.objects.create(name='Laptop',SKU='LP123')
        article2=Article.objects.create(name='Phone',SKU='PH456')

        self.assertEquals(article1.name,'Laptop')
        self.assertEquals(article1.SKU,'LP123')

        self.assertEquals(article2.name,'Phone')
        self.assertEquals(article2.SKU,'PH456')
