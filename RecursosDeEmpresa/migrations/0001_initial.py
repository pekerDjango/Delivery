# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoDocumento'
        db.create_table(u'RecursosDeEmpresa_tipodocumento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['TipoDocumento'])

        # Adding model 'Barrio'
        db.create_table(u'RecursosDeEmpresa_barrio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Barrio'])

        # Adding model 'Localidad'
        db.create_table(u'RecursosDeEmpresa_localidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Localidad'])

        # Adding M2M table for field barrio on 'Localidad'
        m2m_table_name = db.shorten_name(u'RecursosDeEmpresa_localidad_barrio')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('localidad', models.ForeignKey(orm[u'RecursosDeEmpresa.localidad'], null=False)),
            ('barrio', models.ForeignKey(orm[u'RecursosDeEmpresa.barrio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['localidad_id', 'barrio_id'])

        # Adding model 'Provincia'
        db.create_table(u'RecursosDeEmpresa_provincia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Provincia'])

        # Adding M2M table for field localidad on 'Provincia'
        m2m_table_name = db.shorten_name(u'RecursosDeEmpresa_provincia_localidad')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('provincia', models.ForeignKey(orm[u'RecursosDeEmpresa.provincia'], null=False)),
            ('localidad', models.ForeignKey(orm[u'RecursosDeEmpresa.localidad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['provincia_id', 'localidad_id'])

        # Adding model 'Persona'
        db.create_table(u'RecursosDeEmpresa_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.TipoDocumento'])),
            ('numero_documento', self.gf('django.db.models.fields.IntegerField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('numero_direccion', self.gf('django.db.models.fields.IntegerField')()),
            ('piso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('depto', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Provincia'])),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Localidad'])),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Barrio'])),
            ('telefono_particular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telefono_domicilio', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Persona'])

        # Adding model 'Turno'
        db.create_table(u'RecursosDeEmpresa_turno', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Turno'])

        # Adding model 'CalificacionServicio'
        db.create_table(u'RecursosDeEmpresa_calificacionservicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['CalificacionServicio'])

        # Adding model 'Sucursal'
        db.create_table(u'RecursosDeEmpresa_sucursal', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('numero_direccion', self.gf('django.db.models.fields.IntegerField')()),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Barrio'])),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Localidad'])),
            ('calificacion_servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.CalificacionServicio'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Sucursal'])

        # Adding model 'TelefonoSucursal'
        db.create_table(u'RecursosDeEmpresa_telefonosucursal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Sucursal'])),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['TelefonoSucursal'])

        # Adding model 'Empleado'
        db.create_table(u'RecursosDeEmpresa_empleado', (
            (u'persona_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['RecursosDeEmpresa.Persona'], unique=True)),
            ('legajo', self.gf('django.db.models.fields.IntegerField')(unique=True, primary_key=True)),
            ('turno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Turno'])),
            ('sucursal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Sucursal'])),
        ))
        db.send_create_signal(u'RecursosDeEmpresa', ['Empleado'])


    def backwards(self, orm):
        # Deleting model 'TipoDocumento'
        db.delete_table(u'RecursosDeEmpresa_tipodocumento')

        # Deleting model 'Barrio'
        db.delete_table(u'RecursosDeEmpresa_barrio')

        # Deleting model 'Localidad'
        db.delete_table(u'RecursosDeEmpresa_localidad')

        # Removing M2M table for field barrio on 'Localidad'
        db.delete_table(db.shorten_name(u'RecursosDeEmpresa_localidad_barrio'))

        # Deleting model 'Provincia'
        db.delete_table(u'RecursosDeEmpresa_provincia')

        # Removing M2M table for field localidad on 'Provincia'
        db.delete_table(db.shorten_name(u'RecursosDeEmpresa_provincia_localidad'))

        # Deleting model 'Persona'
        db.delete_table(u'RecursosDeEmpresa_persona')

        # Deleting model 'Turno'
        db.delete_table(u'RecursosDeEmpresa_turno')

        # Deleting model 'CalificacionServicio'
        db.delete_table(u'RecursosDeEmpresa_calificacionservicio')

        # Deleting model 'Sucursal'
        db.delete_table(u'RecursosDeEmpresa_sucursal')

        # Deleting model 'TelefonoSucursal'
        db.delete_table(u'RecursosDeEmpresa_telefonosucursal')

        # Deleting model 'Empleado'
        db.delete_table(u'RecursosDeEmpresa_empleado')


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