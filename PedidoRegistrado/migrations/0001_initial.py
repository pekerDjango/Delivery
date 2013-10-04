# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Servicio'
        db.create_table(u'PedidoRegistrado_servicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['Servicio'])

        # Adding model 'TipologiaVivienda'
        db.create_table(u'PedidoRegistrado_tipologiavivienda', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['TipologiaVivienda'])

        # Adding model 'DomicilioSearch'
        db.create_table(u'PedidoRegistrado_domiciliosearch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('numero_direccion', self.gf('django.db.models.fields.IntegerField')()),
            ('piso', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('depto', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('localidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Localidad'])),
            ('barrio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['RecursosDeEmpresa.Barrio'])),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['DomicilioSearch'])

        # Adding model 'Cliente'
        db.create_table(u'PedidoRegistrado_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('telefono_particular', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['Cliente'])

        # Adding model 'EstadoPedido'
        db.create_table(u'PedidoRegistrado_estadopedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['EstadoPedido'])

        # Adding model 'Pedido'
        db.create_table(u'PedidoRegistrado_pedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.Cliente'])),
            ('fechaPedido', self.gf('django.db.models.fields.DateTimeField')()),
            ('hora_entrega', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.EstadoPedido'])),
            ('servicio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.Servicio'])),
            ('tipologia_vivienda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.TipologiaVivienda'])),
            ('precio_envio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['Pedido'])

        # Adding model 'DetallePedido'
        db.create_table(u'PedidoRegistrado_detallepedido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pedido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.Pedido'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.DetalleVersiones'], null=True, blank=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Menu'], null=True, blank=True)),
            ('promocion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Promocion'], null=True, blank=True)),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['DetallePedido'])

        # Adding model 'ProductoParaArmar'
        db.create_table(u'PedidoRegistrado_productoparaarmar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoProducto'])),
            ('slogan', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Version'])),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['ProductoParaArmar'])

        # Adding model 'DetalleVersiones'
        db.create_table(u'PedidoRegistrado_detalleversiones', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'pedidoregistrado_detalleversiones_related', to=orm['ComponentesDePedido.Clasificacion'])),
            ('precio', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.ProductoParaArmar'])),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['DetalleVersiones'])

        # Adding model 'SeccionProducto'
        db.create_table(u'PedidoRegistrado_seccionproducto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.ProductoParaArmar'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
            ('tipoIngrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.TipoIngrediente'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('obligatoria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('excluyente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cantidad_exclusiones', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['SeccionProducto'])

        # Adding model 'IngredientesSeccion'
        db.create_table(u'PedidoRegistrado_ingredientesseccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.SeccionProducto'])),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Ingrediente'])),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ComponentesDePedido.Clasificacion'])),
            ('cantidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['IngredientesSeccion'])

        # Adding model 'ProductoArmado'
        db.create_table(u'PedidoRegistrado_productoarmado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.ProductoParaArmar'])),
            ('version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.DetalleVersiones'])),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['ProductoArmado'])

        # Adding model 'DetalleProductoArmado'
        db.create_table(u'PedidoRegistrado_detalleproductoarmado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.ProductoArmado'])),
            ('ingrediente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PedidoRegistrado.IngredientesSeccion'])),
        ))
        db.send_create_signal(u'PedidoRegistrado', ['DetalleProductoArmado'])


    def backwards(self, orm):
        # Deleting model 'Servicio'
        db.delete_table(u'PedidoRegistrado_servicio')

        # Deleting model 'TipologiaVivienda'
        db.delete_table(u'PedidoRegistrado_tipologiavivienda')

        # Deleting model 'DomicilioSearch'
        db.delete_table(u'PedidoRegistrado_domiciliosearch')

        # Deleting model 'Cliente'
        db.delete_table(u'PedidoRegistrado_cliente')

        # Deleting model 'EstadoPedido'
        db.delete_table(u'PedidoRegistrado_estadopedido')

        # Deleting model 'Pedido'
        db.delete_table(u'PedidoRegistrado_pedido')

        # Deleting model 'DetallePedido'
        db.delete_table(u'PedidoRegistrado_detallepedido')

        # Deleting model 'ProductoParaArmar'
        db.delete_table(u'PedidoRegistrado_productoparaarmar')

        # Deleting model 'DetalleVersiones'
        db.delete_table(u'PedidoRegistrado_detalleversiones')

        # Deleting model 'SeccionProducto'
        db.delete_table(u'PedidoRegistrado_seccionproducto')

        # Deleting model 'IngredientesSeccion'
        db.delete_table(u'PedidoRegistrado_ingredientesseccion')

        # Deleting model 'ProductoArmado'
        db.delete_table(u'PedidoRegistrado_productoarmado')

        # Deleting model 'DetalleProductoArmado'
        db.delete_table(u'PedidoRegistrado_detalleproductoarmado')


    models = {
        u'ComponentesDePedido.clasificacion': {
            'Meta': {'object_name': 'Clasificacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ComponentesDePedido.detalleversiones': {
            'Meta': {'object_name': 'DetalleVersiones'},
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'componentesdepedido_detalleversiones_related'", 'to': u"orm['ComponentesDePedido.Clasificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagenProducto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Producto']"})
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
        },
        u'PedidoRegistrado.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'telefono_particular': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'PedidoRegistrado.detallepedido': {
            'Meta': {'object_name': 'DetallePedido'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Menu']", 'null': 'True', 'blank': 'True'}),
            'pedido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.Pedido']"}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.DetalleVersiones']", 'null': 'True', 'blank': 'True'}),
            'promocion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Promocion']", 'null': 'True', 'blank': 'True'})
        },
        u'PedidoRegistrado.detalleproductoarmado': {
            'Meta': {'object_name': 'DetalleProductoArmado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.IngredientesSeccion']"}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.ProductoArmado']"})
        },
        u'PedidoRegistrado.detalleversiones': {
            'Meta': {'object_name': 'DetalleVersiones'},
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'pedidoregistrado_detalleversiones_related'", 'to': u"orm['ComponentesDePedido.Clasificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.ProductoParaArmar']"})
        },
        u'PedidoRegistrado.domiciliosearch': {
            'Meta': {'object_name': 'DomicilioSearch'},
            'barrio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Barrio']"}),
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'depto': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['RecursosDeEmpresa.Localidad']"}),
            'numero_direccion': ('django.db.models.fields.IntegerField', [], {}),
            'piso': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'PedidoRegistrado.estadopedido': {
            'Meta': {'object_name': 'EstadoPedido'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'PedidoRegistrado.ingredientesseccion': {
            'Meta': {'object_name': 'IngredientesSeccion'},
            'cantidad': ('django.db.models.fields.IntegerField', [], {}),
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Clasificacion']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Ingrediente']"}),
            'seccion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.SeccionProducto']"})
        },
        u'PedidoRegistrado.pedido': {
            'Meta': {'object_name': 'Pedido'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.Cliente']"}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.EstadoPedido']"}),
            'fechaPedido': ('django.db.models.fields.DateTimeField', [], {}),
            'hora_entrega': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_envio': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'servicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.Servicio']"}),
            'tipologia_vivienda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.TipologiaVivienda']"})
        },
        u'PedidoRegistrado.productoarmado': {
            'Meta': {'object_name': 'ProductoArmado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.ProductoParaArmar']"}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.DetalleVersiones']"})
        },
        u'PedidoRegistrado.productoparaarmar': {
            'Meta': {'object_name': 'ProductoParaArmar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slogan': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tipo_producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoProducto']"}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.Version']"})
        },
        u'PedidoRegistrado.seccionproducto': {
            'Meta': {'object_name': 'SeccionProducto'},
            'cantidad_exclusiones': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'excluyente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'obligatoria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PedidoRegistrado.ProductoParaArmar']"}),
            'tipoIngrediente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ComponentesDePedido.TipoIngrediente']"})
        },
        u'PedidoRegistrado.servicio': {
            'Meta': {'object_name': 'Servicio'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'PedidoRegistrado.tipologiavivienda': {
            'Meta': {'object_name': 'TipologiaVivienda'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['PedidoRegistrado']