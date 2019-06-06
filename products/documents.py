from elasticsearch_dsl import Index, DocType
posts = Index('posts')

@posts.doc_type
class PostDocument(DocType):

    class Meta:

        fields = [
            'title',
        ]
