# -*- coding: utf-8 -*-
from odoo import http

# class ChadMod(http.Controller):
#     @http.route('/chad_mod/chad_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chad_mod/chad_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chad_mod.listing', {
#             'root': '/chad_mod/chad_mod',
#             'objects': http.request.env['chad_mod.chad_mod'].search([]),
#         })

#     @http.route('/chad_mod/chad_mod/objects/<model("chad_mod.chad_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chad_mod.object', {
#             'object': obj
#         })