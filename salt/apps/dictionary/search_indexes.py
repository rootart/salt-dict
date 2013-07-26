from haystack import indexes

from dictionary.models import Definition


class DefinitionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.NgramField(document=True, use_template=True)

    def get_model(self):
        return Definition

    def index_queryset(self, using=None):
        return self.get_model().objects.all()