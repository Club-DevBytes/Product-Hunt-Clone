from elasticsearch_dsl import Document
from elasticsearch_dsl import Index


from .models import Product
from elasticsearch_dsl.connections import connections
connections.create_connection()

posts = Index('posts')

@posts.document
class PostDocument(Document):

         
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