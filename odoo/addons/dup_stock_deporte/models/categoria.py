from odoo import models, fields

class Categoria(models.Model):
    _name = 'dup_stock_deporte.categoria'
    _description = 'Categoría de Productos Deportivos'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    producto_ids = fields.One2many('dup_stock_deporte.producto', 'categoria_id', string='Productos')
