from odoo import models, fields

class Almacen(models.Model):
    _name = 'dup_stock_deporte.almacen'
    _description = 'Almacén de Productos Deportivos'

    name = fields.Char(string='Nombre', required=True)
    ubicacion = fields.Char(string='Ubicación')
    productos = fields.Many2many('dup_stock_deporte.producto', string='Productos Almacenados')
