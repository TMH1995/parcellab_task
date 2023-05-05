from shipping.models import Article

class ArticleImportService:

    def handleArticleFetch(self,name:str,SKU:str)->Article:
        article,_= Article.objects.get_or_create(name=name,SKU=SKU)
        
        return article