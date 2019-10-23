from elasticsearch_dsl import DocType
from django_elasticsearch_dsl import Index
from  .models import Product
posts = Index('posts')

@posts.doc_type
class PostDocument(DocType):
    class Index:
        # Name of the Elasticsearch index

        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Product
        fields = [
            'title',
        ]