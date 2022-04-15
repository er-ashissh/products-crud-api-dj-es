from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from products.models import ProductDetails


@registry.register_document
class ProductDetailsDocument(Document):
    id = fields.IntegerField(attr='id')
    name = fields.TextField(attr='name', fields={'suggest': fields.Completion()})
    price = fields.IntegerField()
    quantity = fields.IntegerField()

    class Index:
        name = 'product_details'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = ProductDetails