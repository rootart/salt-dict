from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import fields

from .models import Definition, DefinitionSource


class DefinitionSourceResource(ModelResource):
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


v1_api = Api(api_name='v1')
v1_api.register(DefinitionResource())
