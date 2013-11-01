# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ExUserProfile.ofertasYPromocionesDisponibles'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'ofertasYPromocionesDisponibles',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ExUserProfile.menuDiario'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'menuDiario',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ExUserProfile.notificacionPedidosConfirmados'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'notificacionPedidosConfirmados',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ExUserProfile.estadoPedidosRealizados'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'estadoPedidosRealizados',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ExUserProfile.ofertasYPromocionesDisponibles'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'ofertasYPromocionesDisponibles')

        # Deleting field 'ExUserProfile.menuDiario'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'menuDiario')

        # Deleting field 'ExUserProfile.notificacionPedidosConfirmados'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'notificacionPedidosConfirmados')

        # Deleting field 'ExUserProfile.estadoPedidosRealizados'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'estadoPedidosRealizados')


    models = {
        u'ConfiguracionDeComponentes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Barrio']"}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'depto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'estadoPedidosRealizados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'menuDiario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'notificacionPedidosConfirmados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {}),
            'ofertasYPromocionesDisponibles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono_domicilio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono_particular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'Usuario Asociado'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'ConfiguracionDeComponentes.exuserprofile': {
            'Meta': {'object_name': 'ExUserProfile'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Barrio']"}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'depto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'estadoPedidosRealizados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 1, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'menuDiario': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'notificacionPedidosConfirmados': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {}),
            'ofertasYPromocionesDisponibles': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono_domicilio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telefono_particular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'RecursosDeEmpresa.barrio': {
            'Meta': {'object_name': 'Barrio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'RecursosDeEmpresa.localidad': {
            'Meta': {'object_name': 'Localidad'},
            'barrio': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['RecursosDeEmpresa.Barrio']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
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