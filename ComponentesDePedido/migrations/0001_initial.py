# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoIngrediente'
        db.create_table(u'ComponentesDePedido_tipoingrediente', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['TipoIngrediente'])

        # Adding model 'Clasificacion'
        db.create_table(u'ComponentesDePedido_clasificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Clasificacion'])

        # Adding model 'Version'
        db.create_table(u'ComponentesDePedido_version', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Version'])

        # Adding M2M table for field clasificacion on 'Version'
        m2m_table_name = db.shorten_name(u'ComponentesDePedido_version_clasificacion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('version', models.ForeignKey(orm[u'ComponentesDePedido.version'], null=False)),
            ('clasificacion', models.ForeignKey(orm[u'ComponentesDePedido.clasificacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['version_id', 'clasificacion_id'])

        # Adding model 'UnidadDeMedida'
        db.create_table(u'ComponentesDePedido_unidaddemedida', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['UnidadDeMedida'])

        # Adding model 'TipoProducto'
        db.create_table(u'ComponentesDePedido_tipoproducto', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['TipoProducto'])

        # Adding model 'Ingrediente'
        db.create_table(u'ComponentesDePedido_ingrediente', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tipoIngrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoIngrediente'])),
            ('unidadDeMedida', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.UnidadDeMedida'])),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('stockActual', self.gf('django.db.models.fields.IntegerField')()),
            ('stockMinimo', self.gf('django.db.models.fields.IntegerField')()),
            ('stockCorte', self.gf('django.db.models.fields.IntegerField')()),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Ingrediente'])

        # Adding model 'Producto'
        db.create_table(u'ComponentesDePedido_producto', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tiempoPreparacion', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('tipoProducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoProducto'])),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Version'])),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Producto'])

        # Adding model 'DetalleIngredientes'
        db.create_table(u'ComponentesDePedido_detalleingredientes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipoIngrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoIngrediente'])),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Ingrediente'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DetalleIngredientes'])

        # Adding model 'DetalleVersiones'
        db.create_table(u'ComponentesDePedido_detalleversiones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'componentesdepedido_detalleversiones_related', to=orm['ComponentesDePedido.Clasificacion'])),
            ('imagenProducto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto'])),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DetalleVersiones'])

        # Adding model 'Menu'
        db.create_table(u'ComponentesDePedido_menu', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('precioVenta', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Menu'])

        # Adding model 'DetalleMenu'
        db.create_table(u'ComponentesDePedido_detallemenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Menu'])),
            ('tipoProducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoProducto'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto'])),
            ('versionProducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Clasificacion'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DetalleMenu'])

        # Adding model 'Frecuencia'
        db.create_table(u'ComponentesDePedido_frecuencia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Frecuencia'])

        # Adding model 'Promocion'
        db.create_table(u'ComponentesDePedido_promocion', (
            ('codigo', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('stock', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tiempoPreparacion', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Promocion'])

        # Adding model 'DiaSemana'
        db.create_table(u'ComponentesDePedido_diasemana', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DiaSemana'])

        # Adding model 'Programacion'
        db.create_table(u'ComponentesDePedido_programacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fechaDesde', self.gf('django.db.models.fields.DateField')()),
            ('fechaHasta', self.gf('django.db.models.fields.DateField')()),
            ('horaDesde', self.gf('django.db.models.fields.TimeField')()),
            ('horaHasta', self.gf('django.db.models.fields.TimeField')()),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Promocion'])),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['Programacion'])

        # Adding M2M table for field diaSemana on 'Programacion'
        m2m_table_name = db.shorten_name(u'ComponentesDePedido_programacion_diaSemana')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('programacion', models.ForeignKey(orm[u'ComponentesDePedido.programacion'], null=False)),
            ('diasemana', models.ForeignKey(orm[u'ComponentesDePedido.diasemana'], null=False))
        ))
        db.create_unique(m2m_table_name, ['programacion_id', 'diasemana_id'])

        # Adding model 'DetallePromocionProducto'
        db.create_table(u'ComponentesDePedido_detallepromocionproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Promocion'])),
            ('tipoProducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoProducto'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto'])),
            ('versionProducto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Clasificacion'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DetallePromocionProducto'])

        # Adding model 'DetallePromocionMenu'
        db.create_table(u'ComponentesDePedido_detallepromocionmenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Promocion'])),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Menu'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ComponentesDePedido', ['DetallePromocionMenu'])


    def backwards(self, orm):
        # Deleting model 'TipoIngrediente'
        db.delete_table(u'ComponentesDePedido_tipoingrediente')

        # Deleting model 'Clasificacion'
        db.delete_table(u'ComponentesDePedido_clasificacion')

        # Deleting model 'Version'
        db.delete_table(u'ComponentesDePedido_version')

        # Removing M2M table for field clasificacion on 'Version'
        db.delete_table(db.shorten_name(u'ComponentesDePedido_version_clasificacion'))

        # Deleting model 'UnidadDeMedida'
        db.delete_table(u'ComponentesDePedido_unidaddemedida')

        # Deleting model 'TipoProducto'
        db.delete_table(u'ComponentesDePedido_tipoproducto')

        # Deleting model 'Ingrediente'
        db.delete_table(u'ComponentesDePedido_ingrediente')

        # Deleting model 'Producto'
        db.delete_table(u'ComponentesDePedido_producto')

        # Deleting model 'DetalleIngredientes'
        db.delete_table(u'ComponentesDePedido_detalleingredientes')

        # Deleting model 'DetalleVersiones'
        db.delete_table(u'ComponentesDePedido_detalleversiones')

        # Deleting model 'Menu'
        db.delete_table(u'ComponentesDePedido_menu')

        # Deleting model 'DetalleMenu'
        db.delete_table(u'ComponentesDePedido_detallemenu')

        # Deleting model 'Frecuencia'
        db.delete_table(u'ComponentesDePedido_frecuencia')

        # Deleting model 'Promocion'
        db.delete_table(u'ComponentesDePedido_promocion')

        # Deleting model 'DiaSemana'
        db.delete_table(u'ComponentesDePedido_diasemana')

        # Deleting model 'Programacion'
        db.delete_table(u'ComponentesDePedido_programacion')

        # Removing M2M table for field diaSemana on 'Programacion'
        db.delete_table(db.shorten_name(u'ComponentesDePedido_programacion_diaSemana'))

        # Deleting model 'DetallePromocionProducto'
        db.delete_table(u'ComponentesDePedido_detallepromocionproducto')

        # Deleting model 'DetallePromocionMenu'
        db.delete_table(u'ComponentesDePedido_detallepromocionmenu')


    models = {
        u'ComponentesDePedido.clasificacion': {
            'Meta': {'object_name': 'Clasificacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ComponentesDePedido.detalleingredientes': {
            'Meta': {'object_name': 'DetalleIngredientes'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Ingrediente']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
            'tipoIngrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoIngrediente']"})
        },
        u'ComponentesDePedido.detallemenu': {
            'Meta': {'object_name': 'DetalleMenu'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Menu']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
            'tipoProducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoProducto']"}),
            'versionProducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Clasificacion']"})
        },
        u'ComponentesDePedido.detallepromocionmenu': {
            'Meta': {'object_name': 'DetallePromocionMenu'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Menu']"}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Promocion']"})
        },
        u'ComponentesDePedido.detallepromocionproducto': {
            'Meta': {'object_name': 'DetallePromocionProducto'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Promocion']"}),
            'tipoProducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoProducto']"}),
            'versionProducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Clasificacion']"})
        },
        u'ComponentesDePedido.detalleversiones': {
            'Meta': {'object_name': 'DetalleVersiones'},
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'componentesdepedido_detalleversiones_related'", 'to': u"orm['ComponentesDePedido.Clasificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagenProducto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"})
        },
        u'ComponentesDePedido.diasemana': {
            'Meta': {'object_name': 'DiaSemana'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ComponentesDePedido.frecuencia': {
            'Meta': {'object_name': 'Frecuencia'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ComponentesDePedido.ingrediente': {
            'Meta': {'object_name': 'Ingrediente'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'stockActual': ('django.db.models.fields.IntegerField', [], {}),
            'stockCorte': ('django.db.models.fields.IntegerField', [], {}),
            'stockMinimo': ('django.db.models.fields.IntegerField', [], {}),
            'tipoIngrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoIngrediente']"}),
            'unidadDeMedida': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.UnidadDeMedida']"})
        },
        u'ComponentesDePedido.menu': {
            'Meta': {'object_name': 'Menu'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precioVenta': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'ComponentesDePedido.producto': {
            'Meta': {'object_name': 'Producto'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tiempoPreparacion': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'tipoProducto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoProducto']"}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Version']"})
        },
        u'ComponentesDePedido.programacion': {
            'Meta': {'object_name': 'Programacion'},
            'diaSemana': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ComponentesDePedido.DiaSemana']", 'symmetrical': 'False'}),
            'fechaDesde': ('django.db.models.fields.DateField', [], {}),
            'fechaHasta': ('django.db.models.fields.DateField', [], {}),
            'horaDesde': ('django.db.models.fields.TimeField', [], {}),
            'horaHasta': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Promocion']"})
        },
        u'ComponentesDePedido.promocion': {
            'Meta': {'object_name': 'Promocion'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'stock': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tiempoPreparacion': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ComponentesDePedido.tipoingrediente': {
            'Meta': {'object_name': 'TipoIngrediente'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ComponentesDePedido.tipoproducto': {
            'Meta': {'object_name': 'TipoProducto'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ComponentesDePedido.unidaddemedida': {
            'Meta': {'object_name': 'UnidadDeMedida'},
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ComponentesDePedido.version': {
            'Meta': {'object_name': 'Version'},
            'clasificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ComponentesDePedido.Clasificacion']", 'symmetrical': 'False'}),
            'codigo': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['ComponentesDePedido']