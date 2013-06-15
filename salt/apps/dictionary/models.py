from django.db import models


class  Source(models.Model):
    name = models.CharField(blank=True, max_length=100)
    full_name = models.CharField(blank=True, max_length=100)
    


class Definition(models.Model):
    name_ru = models.CharField(blank=True, max_length=255)
    name_en = models.CharField(blank=True, max_length=255)
    name_de = models.CharField(blank=True, max_length=255)
    
    def __unicode__(self):
        return "%s %s %s" % (self.name_ru, self.name_en, self.name_de)
    


class DefinitionSource(models.Model):
    definition = models.ForeignKey(Definition)
    text = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source)
    bib_info = models.CharField(blank=True, max_length=255)


