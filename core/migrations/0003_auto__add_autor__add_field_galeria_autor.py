# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Autor'
        db.create_table(u'core_autor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordenacao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Autor'])

        # Adding field 'Galeria.autor'
        db.add_column(u'core_galeria', 'autor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Autor'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Autor'
        db.delete_table(u'core_autor')

        # Deleting field 'Galeria.autor'
        db.delete_column(u'core_galeria', 'autor_id')


    models = {
        u'core.autor': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Autor'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
        }
    }

    complete_apps = ['core']