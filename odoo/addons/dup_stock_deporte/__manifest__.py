# -*- coding: utf-8 -*-
{
    'name': 'Gestión de Stock Deportivo',
    'version': '1.0',
    'category': 'Inventario',
    'summary': 'Módulo para gestionar el stock de productos deportivos',
    'description': 'Este módulo permite gestionar almacenes, categorías, productos y proveedores de stock deportivo.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/almacen_views.xml',
        'views/categoria_views.xml',
        'views/producto_views.xml',
        'views/proveedor_views.xml',
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
}




