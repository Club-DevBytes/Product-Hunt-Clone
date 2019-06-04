from django_elasticsearch_dsl import DocType, Index
from django_elasticsearch_dsl import Index
from elasticsearch_dsl import Date, Keyword, Text

from .models import Product

posts = Index('posts')

@posts.doc_type
class PostDocument(DocType):

         
    class Index:
        # Name of the Elasticsearch index

        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Meta:
        model = Product

        fields = [
            'title',
            'body',
        ]