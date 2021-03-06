# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Definition.created'
        db.add_column(u'dictionary_definition', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Definition.modefied'
        db.add_column(u'dictionary_definition', 'modefied',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True),
                      keep_default=False)

        # Adding index on 'Definition', fields ['name_ru']
        db.create_index(u'dictionary_definition', ['name_ru'])

        # Adding index on 'Definition', fields ['name_en']
        db.create_index(u'dictionary_definition', ['name_en'])

        # Adding index on 'Definition', fields ['name_de']
        db.create_index(u'dictionary_definition', ['name_de'])


    def backwards(self, orm):
        # Removing index on 'Definition', fields ['name_de']
        db.delete_index(u'dictionary_definition', ['name_de'])

        # Removing index on 'Definition', fields ['name_en']
        db.delete_index(u'dictionary_definition', ['name_en'])

        # Removing index on 'Definition', fields ['name_ru']
        db.delete_index(u'dictionary_definition', ['name_ru'])

        # Deleting field 'Definition.created'
        db.delete_column(u'dictionary_definition', 'created')

        # Deleting field 'Definition.modefied'
        db.delete_column(u'dictionary_definition', 'modefied')


    models = {
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modefied': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'name_de': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'})
        },
        u'dictionary.definitionsource': {
            'Meta': {'object_name': 'DefinitionSource'},
            'bib_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources'", 'to': u"orm['dictionary.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Source']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'dictionary.source': {
            'Meta': {'object_name': 'Source'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['dictionary']