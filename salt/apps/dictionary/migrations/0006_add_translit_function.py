# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.db import connection


class Migration(DataMigration):

    def forwards(self, orm):
        cursor = connection.cursor()
        sql = \
        """
        CREATE OR REPLACE FUNCTION iris_translit(p_string character varying)
              RETURNS character varying AS
            $BODY$
            --Транслитерация
            --Отличие от ГОСТ 7.79-2000
            --ё = e, а не yo
            --ы = y`, а не y'
            select 
                    replace(
                    replace(
                    replace(
                    replace(
                    replace(
                    replace(
                    replace(
                    replace(
                    replace(
                        translate(lower($1), 
                        'абвгдеёзийклмнопрстуфхць ,.', 'abvgdeezijklmnoprstufхc---'),
                        'ж', 'zh'),
                        'ч', 'ch'),
                        'ш', 'sh'),
                        'щ', 'shh'),
                        'ъ', '-'),
                        'ы', 'y-'),
                        'э', 'e-'),
                        'ю', 'yu'),
                        'я', 'ya');
            $BODY$
          LANGUAGE sql IMMUTABLE
          COST 100;
        """
        cursor.execute(sql)

    def backwards(self, orm):
        cursor = connection.cursor()
        sql = """ DROP FUNCTION IF EXISTS iris_translit(p_string character varying)"""
        cursor.execute(sql)

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
            'Meta': {'ordering': "['position']", 'object_name': 'DefinitionSource'},
            'bib_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sources'", 'to': u"orm['dictionary.Definition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
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
    symmetrical = True
