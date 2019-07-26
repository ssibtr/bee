# -*- coding: utf-8 -*-
from odoo import http

class Trello(http.Controller):
    @http.route('/trello/trello/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/trello/trello/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('trello.listing', {
            'root': '/trello/trello',
            'objects': http.request.env['trello.trello'].search([]),
        })

    @http.route('/trello/trello/objects/<model("trello.trello"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('trello.object', {
            'object': obj
        })