# -*- coding: utf-8 -*-
{
    'name': "Gestión de Stock para Deportes",
    'summary': "Módulo para gestionar stock de productos deportivos",
    'description': "Este módulo permite gestionar el stock de productos deportivos en Odoo.",
    'author': "DUP",
    'category': 'Inventario',
    'version': '1.0',
    'depends': ['base', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/producto_view.xml',
        'views/categoria_view.xml',
        'views/proveedor_view.xml',
        'views/almacen_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}


