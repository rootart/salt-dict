# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Source'
        db.create_table(u'dictionary_source', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Source'])

        # Adding model 'Definition'
        db.create_table(u'dictionary_definition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_ru', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('name_de', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['Definition'])

        # Adding model 'DefinitionSource'
        db.create_table(u'dictionary_definitionsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('definition', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Definition'])),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dictionary.Source'])),
            ('bib_info', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'dictionary', ['DefinitionSource'])


    def backwards(self, orm):
        # Deleting model 'Source'
        db.delete_table(u'dictionary_source')

        # Deleting model 'Definition'
        db.delete_table(u'dictionary_definition')

        # Deleting model 'DefinitionSource'
        db.delete_table(u'dictionary_definitionsource')


    models = {
        u'dictionary.definition': {
            'Meta': {'object_name': 'Definition'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_de': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'dictionary.definitionsource': {
            'Meta': {'object_name': 'DefinitionSource'},
            'bib_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dictionary.Source']"})
        },
        u'dictionary.source': {
            'Meta': {'object_name': 'Source'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['dictionary']