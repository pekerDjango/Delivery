# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ExUserProfile.is_human'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'is_human')

        # Adding field 'ExUserProfile.telefono_particular'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'telefono_particular',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=100),
                      keep_default=False)

        # Adding field 'ExUserProfile.telefono_domicilio'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'telefono_domicilio',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExUserProfile.fecha_nacimiento'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'fecha_nacimiento',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 31, 0, 0)),
                      keep_default=False)

        # Adding field 'ExUserProfile.sexo'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'sexo',
                      self.gf('django.db.models.fields.CharField')(default='f', max_length=1),
                      keep_default=False)

        # Adding field 'ExUserProfile.direccion'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'direccion',
                      self.gf('django.db.models.fields.CharField')(default='a', max_length=250),
                      keep_default=False)

        # Adding field 'ExUserProfile.numero_direccion'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'numero_direccion',
                      self.gf('django.db.models.fields.IntegerField')(default='2'),
                      keep_default=False)

        # Adding field 'ExUserProfile.piso'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'piso',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExUserProfile.depto'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'depto',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'ExUserProfile.codigo_postal'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'codigo_postal',
                      self.gf('django.db.models.fields.CharField')(default='2', max_length=100),
                      keep_default=False)

        # Adding field 'ExUserProfile.localidad'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'localidad',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['RecursosDeEmpresa.Localidad']),
                      keep_default=False)

        # Adding field 'ExUserProfile.barrio'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'barrio',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['RecursosDeEmpresa.Barrio']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ExUserProfile.is_human'
        db.add_column(u'ConfiguracionDeComponentes_exuserprofile', 'is_human',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'ExUserProfile.telefono_particular'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'telefono_particular')

        # Deleting field 'ExUserProfile.telefono_domicilio'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'telefono_domicilio')

        # Deleting field 'ExUserProfile.fecha_nacimiento'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'fecha_nacimiento')

        # Deleting field 'ExUserProfile.sexo'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'sexo')

        # Deleting field 'ExUserProfile.direccion'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'direccion')

        # Deleting field 'ExUserProfile.numero_direccion'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'numero_direccion')

        # Deleting field 'ExUserProfile.piso'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'piso')

        # Deleting field 'ExUserProfile.depto'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'depto')

        # Deleting field 'ExUserProfile.codigo_postal'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'codigo_postal')

        # Deleting field 'ExUserProfile.localidad'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'localidad_id')

        # Deleting field 'ExUserProfile.barrio'
        db.delete_column(u'ConfiguracionDeComponentes_exuserprofile', 'barrio_id')


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
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 31, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {}),
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