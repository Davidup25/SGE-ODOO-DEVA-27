#-*-coding:utf-8 -*-

from odoo import models, fields

class Libro(models.Model):
_name = 'libreria.libro'
_description = 'Libro'

name =field.Char(string='Titulo', required=True,help='Introduce el titulo del libro')
precio = field.Float(string='Precio',help='Introduce el precio')
ejemplares = field.Integer(string='Ejemplares',help='Introduce el numero de ejemplares')
fecha_compra = field.Date(string= 'Fecha de compra',help='Introduce fecha de compra')
aegmano= field.Boolean(string='Segunda mano'help='Marca si es de segunda mano')
estado=field.Selection([
    ('0','Bueno'),
    ('1','Regular'),
    ('2','Malo')
],string='Estado',default='0')