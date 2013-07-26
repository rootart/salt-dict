from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import fields

from .models import Definition, DefinitionSource
from haystack.query import SearchQuerySet


class DefinitionSourceResource(ModelResource):
    sources = fields.ListField(use_in='detail', default=[])
    class Meta:
        queryset = DefinitionSource.objects.all()
        excludes = ['id',]
        include_resource_uri = False


class DefinitionResource(ModelResource):
    sources = fields.ToManyField(DefinitionSourceResource, 'sources', full=True, null=True,
        related_name='sources', use_in='detail'
    )
    class Meta:
        limit = 100
        queryset = Definition.objects.all()
        resource_name = 'definitions'
        list_allowed_methods = ['get',]
        filtering = {
            'name_ru': ('exact', 'startswith'),
            'name_de': ('exact', 'startswith'),
            'name_en': ('exact', 'startswith')
        }


class SearchDefinitions(ModelResource):
    sources = fields.ListField(use_in='detail', default=[])
    class Meta:
        fields = ('name_ru', 'name_en', 'name_de')
        queryset = Definition.objects.all()
        resource_name = 'search'
        detail_uri_name = 'name_en'


    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(SearchDefinitions, self).build_filters(filters)

        if "q" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])
            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters

    def dehydrate_sources(self, bundle):
        return [
            {'text': i.text, 'bib_info': i.bib_info} for i in  bundle.obj.sources.all()
        ]

v1_api = Api(api_name='v1')
v1_api.register(DefinitionResource())
v1_api.register(SearchDefinitions())
