#-*-coding:utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
    _name = 'libreria.libro'
    _description = 'Libro'

name =fields.Char(string='Titulo', required=True,help='Introduce el titulo del libro')
precio = fields.Float(string='Precio',help='Introduce el precio')
ejemplares = fields.Integer(string='Ejemplares',help='Introduce el numero de ejemplares')
fecha_compra = fields.Date(string= 'Fecha de compra',help='Introduce fecha de compra')
segmano= fields.Boolean(string='Segunda mano',help='Marca si es de segunda mano')
estado=fields.Selection([
    ('0','Bueno'),
    ('1','Regular'),
    ('2','Malo')
],string='Estado',default='0')