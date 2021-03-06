from django.http import HttpResponse

from tastypie.resources import ModelResource
from tastypie.api import Api
from tastypie import fields
from tastypie import resources
from tastypie.exceptions import NotFound

from .models import Definition, DefinitionSource
from haystack.query import SearchQuerySet


def build_content_type(format, encoding='utf-8'):
    """
    Appends character encoding to the provided format if not already present.
    """
    if 'charset' in format:
        return format

    return "%s; charset=%s" % (format, encoding)



class DefinitionSourceResource(ModelResource):
    sources = fields.ListField(use_in='detail', default=[])
    name_ru_slug = fields.CharField(attribute='name_ru_slug', default='', use_in='list')
    class Meta:
        queryset = Definition.objects.all().extra(
            select={
                'name_ru_slug': 'iris_translit(name_ru)'
            }
        )
        excludes = ['id',]
        include_resource_uri = False


class DefinitionResource(ModelResource):
    sources = fields.ToManyField(DefinitionSourceResource, 'sources', full=True, null=True,
        related_name='sources', use_in='detail'
    )
    name_ru_slug = fields.CharField(attribute='name_ru_slug', default='')

    class Meta:
        queryset = Definition.objects.all().extra(
            select={
                'name_ru_slug': 'iris_translit(name_ru)'
            }
        )
        resource_name = 'definitions'
        detail_uri_name = 'name_ru_slug'
        list_allowed_methods = ['get',]
        filtering = {
            'name_ru': ('exact', 'startswith'),
            'name_de': ('exact', 'startswith'),
            'name_en': ('exact', 'startswith')
        }


class SearchDefinitions(ModelResource):
    sources = fields.ListField(use_in='detail', default=[])
    name_ru_slug = fields.CharField(attribute='name_ru_slug', default='')

    class Meta:
        fields = ('name_ru', 'name_en', 'name_de')
        queryset = Definition.objects.all().extra(
            select={
                'name_ru_slug': 'iris_translit(name_ru)'
            }
        )
        resource_name = 'search'
        detail_uri_name = 'name_ru_slug'

    def obj_get(self, bundle, **kwargs):
        try:
            param = kwargs['name_ru_slug']
            object_list = self.get_object_list(bundle.request).extra(
                where = ['iris_translit(name_ru)=\'%s\'' % param]
            )
            if len(object_list) <= 0:
                raise self._meta.object_class.DoesNotExist("Couldn't find an instance of '%s' which matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))
            elif len(object_list) > 1:
                raise MultipleObjectsReturned("More than '%s' matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))

            bundle.obj = object_list[0]
            self.authorized_read_detail(object_list, bundle)
            return bundle.obj
        except ValueError:
            raise NotFound("Invalid resource lookup data provided (mismatched type).")

    def create_response(self, request, data, response_class=HttpResponse, **response_kwargs):
        """
        Extracts the common "which-format/serialize/return-response" cycle.

        Mostly a useful shortcut/hook.
        """
        desired_format = self.determine_format(request)
        serialized = self.serialize(request, data, desired_format)
        return response_class(content=serialized, content_type=build_content_type(desired_format), **response_kwargs)


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
            {'text': i.text, 'bib_info': i.bib_info, 'source': i.source.full_name if i.source else '' } for i in  bundle.obj.sources.all().order_by('position')
        ]

v1_api = Api(api_name='v1')
v1_api.register(DefinitionResource())
v1_api.register(SearchDefinitions())
