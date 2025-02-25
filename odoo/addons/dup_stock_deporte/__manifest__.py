# -*- coding: utf-8 -*-
{
    'name': 'Dup_Stock_Deporte',
    'version': '1.0',
    'category': 'Inventario',
    'summary': 'Módulo para gestionar el stock de productos deportivos',
    'description': 'Este módulo permite gestionar almacenes, categorías, productos y proveedores de stock deportivo.',
    'depends': ['base'],
    'data': [
        'views/menu.xml',
        'security/ir.model.access.csv',
        'views/almacen_view.xml',
        'views/categoria_view.xml',
        'views/producto_view.xml',
        'views/proveedor_view.xml',
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'icon': '/dup_stock_deporte/static/description/icon.png',


}



