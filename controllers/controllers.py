# -*- coding: utf-8 -*-
from odoo import http

# class Tttt(http.Controller):
#     @http.route('/tttt/tttt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tttt/tttt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tttt.listing', {
#             'root': '/tttt/tttt',
#             'objects': http.request.env['tttt.tttt'].search([]),
#         })

#     @http.route('/tttt/tttt/objects/<model("tttt.tttt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tttt.object', {
#             'object': obj
#         })