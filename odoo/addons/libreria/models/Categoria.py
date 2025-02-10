#-*-coding:utf-8 -*-

from odoo import models, fields

class Categoria(models.Model):
    _name = 'libreria.categoria'
    _descripcion = 'Categoria'

    name = fields.Char(string='Nombre', required=True, help='Intreroduce el nombre de la categoria')
    description = fields.Text(string='Descripcion',help='Introduce la descripcion')
    