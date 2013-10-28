# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DetallePromocionProducto.producto'
        db.alter_column(u'ComponentesDePedido_detallepromocionproducto', 'producto_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['ComponentesDePedido.Producto']))

        # Changing field 'DetalleIngredientes.ingrediente'
        db.alter_column(u'ComponentesDePedido_detalleingredientes', 'ingrediente_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['ComponentesDePedido.Ingrediente']))

        # Changing field 'DetalleMenu.producto'
        db.alter_column(u'ComponentesDePedido_detallemenu', 'producto_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['ComponentesDePedido.Producto']))

    def backwards(self, orm):

        # Changing field 'DetallePromocionProducto.producto'
        db.alter_column(u'ComponentesDePedido_detallepromocionproducto', 'producto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto']))

        # Changing field 'DetalleIngredientes.ingrediente'
        db.alter_column(u'ComponentesDePedido_detalleingredientes', 'ingrediente_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Ingrediente']))

        # Changing field 'DetalleMenu.producto'
        db.alter_column(u'ComponentesDePedido_detallemenu', 'producto_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Producto']))

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
            'ingrediente': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['ComponentesDePedido.Ingrediente']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
            'tipoIngrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoIngrediente']"})
        },
        u'ComponentesDePedido.detallemenu': {
            'Meta': {'object_name': 'DetalleMenu'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Menu']"}),
            'producto': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
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
            'producto': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"}),
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