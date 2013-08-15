# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DefinitionSource.source'
        db.alter_column(u'dictionary_definitionsource', 'source_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Source'], null=True))

    def backwards(self, orm):
        pass

    models = {
        u'dictionary.definition': {
            'Meta': {'ordering': "('name_en',)", 'object_name': 'Definition'},
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
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Source']", 'null': 'True', 'blank': 'True'}),
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