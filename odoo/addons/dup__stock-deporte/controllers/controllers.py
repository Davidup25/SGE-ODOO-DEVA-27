# -*- coding: utf-8 -*-
# from odoo import http


# class DupStock-deporte(http.Controller):
#     @http.route('/dup__stock-deporte/dup__stock-deporte', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dup__stock-deporte/dup__stock-deporte/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dup__stock-deporte.listing', {
#             'root': '/dup__stock-deporte/dup__stock-deporte',
#             'objects': http.request.env['dup__stock-deporte.dup__stock-deporte'].search([]),
#         })

#     @http.route('/dup__stock-deporte/dup__stock-deporte/objects/<model("dup__stock-deporte.dup__stock-deporte"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dup__stock-deporte.object', {
#             'object': obj
#         })

