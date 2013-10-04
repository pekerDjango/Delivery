# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'ConfiguracionDeComponentes_usuario', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('empleado', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RecursosDeEmpresa.Empleado'], unique=True)),
        ))
        db.send_create_signal(u'ConfiguracionDeComponentes', ['Usuario'])


    def backwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'ConfiguracionDeComponentes_usuario')


    models = {
        u'ConfiguracionDeComponentes.usuario': {
            'Meta': {'object_name': 'Usuario', '_ormbases': [u'auth.User']},
            'empleado': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['RecursosDeEmpresa.Empleado']", 'unique': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {})
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
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ConfiguracionDeComponentes']