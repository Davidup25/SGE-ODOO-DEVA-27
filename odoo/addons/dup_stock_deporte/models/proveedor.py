from odoo import models, fields

class Proveedor(models.Model):
    _name = 'dup_stock_deporte.proveedor'
    _description = 'Proveedor de Productos'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    producto_ids = fields.One2many('dup_stock_deporte.producto', 'proveedor_id', string='Productos')
