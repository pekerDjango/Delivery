# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sucursal.localizacion'
        db.add_column(u'RecursosDeEmpresa_sucursal', 'localizacion',
                      self.gf('django.db.models.fields.CharField')(default='23141', max_length=250),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sucursal.localizacion'
        db.delete_column(u'RecursosDeEmpresa_sucursal', 'localizacion')


    models = {
        u'RecursosDeEmpresa.barrio': {
            'Meta': {'object_name': 'Barrio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'RecursosDeEmpresa.calificacionservicio': {
            'Meta': {'object_name': 'CalificacionServicio'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'RecursosDeEmpresa.empleado': {
            'Meta': {'object_name': 'Empleado', '_ormbases': [u'RecursosDeEmpresa.Persona']},
            'legajo': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            u'persona_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['RecursosDeEmpresa.Persona']", 'unique': 'True'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Sucursal']"}),
            'turno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Turno']"})
        },
        u'RecursosDeEmpresa.localidad': {
            'Meta': {'object_name': 'Localidad'},
            'barrio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['RecursosDeEmpresa.Barrio']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'RecursosDeEmpresa.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Barrio']"}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'depto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {}),
            'numero_documento': ('django.db.models.fields.IntegerField', [], {'max_length': '100'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Provincia']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono_domicilio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono_particular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.TipoDocumento']"})
        },
        u'RecursosDeEmpresa.provincia': {
            'Meta': {'object_name': 'Provincia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['RecursosDeEmpresa.Localidad']", 'symmetrical': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'RecursosDeEmpresa.sucursal': {
            'Meta': {'object_name': 'Sucursal'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Barrio']"}),
            'calificacion_servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.CalificacionServicio']"}),
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'localizacion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'RecursosDeEmpresa.telefonosucursal': {
            'Meta': {'object_name': 'TelefonoSucursal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sucursal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Sucursal']"})
        },
        u'RecursosDeEmpresa.tipodocumento': {
            'Meta': {'object_name': 'TipoDocumento'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'RecursosDeEmpresa.turno': {
            'Meta': {'object_name': 'Turno'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['RecursosDeEmpresa']