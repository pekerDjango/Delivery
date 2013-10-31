# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Usuario'
       # db.delete_table(u'ConfiguracionDeComponentes_usuario')

        # Adding model 'Cliente'
        db.create_table(u'ConfiguracionDeComponentes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length='30')),
            ('telefono_particular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono_domicilio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length='100')),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('numero_direccion', self.gf('django.db.models.fields.IntegerField')()),
            ('piso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('depto', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Localidad'])),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Barrio'])),
            ('ofertasYPromocionesDisponibles', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('menuDiario', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notificacionPedidosConfirmados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('estadoPedidosRealizados', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(related_name='Usuario Asociado', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'ConfiguracionDeComponentes', ['Cliente'])

        # Adding model 'ExUserProfile'
        db.create_table(u'ConfiguracionDeComponentes_exuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('is_human', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ConfiguracionDeComponentes', ['ExUserProfile'])


    def backwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'ConfiguracionDeComponentes_usuario', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('empleado', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RecursosDeEmpresa.Empleado'], unique=True)),
        ))
        db.send_create_signal(u'ConfiguracionDeComponentes', ['Usuario'])

        # Deleting model 'Cliente'
        db.delete_table(u'ConfiguracionDeComponentes_cliente')

        # Deleting model 'ExUserProfile'
        db.delete_table(u'ConfiguracionDeComponentes_exuserprofile')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_human': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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