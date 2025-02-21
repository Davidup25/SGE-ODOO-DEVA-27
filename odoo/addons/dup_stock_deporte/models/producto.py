from odoo import models, fields

class Producto(models.Model):
    _name = 'dup_stock_deporte.producto'
    _description = 'Producto Deportivo'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio', required=True)
    stock = fields.Integer(string='Stock Disponible')
    categoria_id = fields.Many2one('dup_stock_deporte.categoria', string='Categoría')
    proveedor_id = fields.Many2one('dup_stock_deporte.proveedor', string='Proveedor')
