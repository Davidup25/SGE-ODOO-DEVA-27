# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dup__stock-deporte(models.Model):
#     _name = 'dup__stock-deporte.dup__stock-deporte'
#     _description = 'dup__stock-deporte.dup__stock-deporte'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

