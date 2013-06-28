# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Galeria'
        db.create_table(u'core_galeria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ordenacao', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('imagem', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('ativo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_atualizacao', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Galeria'])


    def backwards(self, orm):
        # Deleting model 'Galeria'
        db.delete_table(u'core_galeria')


    models = {
        u'core.galeria': {
            'Meta': {'ordering': "['ordenacao', 'nome']", 'object_name': 'Galeria'},
            'ativo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data_atualizacao': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ordenacao': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']