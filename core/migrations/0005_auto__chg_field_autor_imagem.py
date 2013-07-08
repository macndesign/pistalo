# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Autor.imagem'
        db.alter_column(u'core_autor', 'imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):

        # Changing field 'Autor.imagem'
        db.alter_column(u'core_autor', 'imagem', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100))

    models = {
        u'core.autor': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Autor'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'core.galeria': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Galeria'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Autor']", 'null': 'True', 'blank': 'True'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'core.sugestao': {
            'Meta': {'ordering': "['ordenacao', 'titulo']", 'object_name': 'Sugestao'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['core']