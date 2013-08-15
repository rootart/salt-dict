from datetime import datetime

from django.db import models
from django.utils.translation import ugettext as _


class  Source(models.Model):
    name = models.CharField(_('source name'), blank=True, max_length=100)
    full_name = models.CharField(_('source full name'), blank=True, max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name=_("Source")
        verbose_name_plural=_('Sources')


class Definition(models.Model):
    name_ru = models.CharField(_('name RU'), blank=True, max_length=255,
        db_index=True
    )
    name_en = models.CharField(_('name EN'), blank=True, max_length=255,
        db_index=True
    )
    name_de = models.CharField(_('name DE'), blank=True, max_length=255,
        db_index=True
    )
    created = models.DateTimeField(auto_now_add=True, default=datetime.now)
    modefied = models.DateTimeField(auto_now=True, default=datetime.now)

    def __unicode__(self):
        return "%s %s %s" % (self.name_ru, self.name_en, self.name_de)

    class Meta:
        verbose_name=_("Definition")
        verbose_name_plural=_('Definitions')
        ordering=('name_en',)


class DefinitionSource(models.Model):
    definition = models.ForeignKey(Definition,
        verbose_name=_('definition'), related_name='sources'
    )
    text = models.TextField(blank=True, null=True,
        verbose_name=_('definition text')
    )
    source = models.ForeignKey(Source,
        verbose_name=_('source'), blank=True, null=True
    )
    bib_info = models.CharField(_('bib info'),
        blank=True, max_length=255
    )

    def __unicode__(self):
        return "%s - %s" % (self.definition.name_ru, self.source.name)

    class Meta:
        verbose_name=_("Definition source")
        verbose_name_plural=_('Definition sources')
