# -*- coding: utf-8 -*-
from odoo import http

# class DbCornRetrieve(http.Controller):
#     @http.route('/db_corn_retrieve/db_corn_retrieve/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/db_corn_retrieve/db_corn_retrieve/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('db_corn_retrieve.listing', {
#             'root': '/db_corn_retrieve/db_corn_retrieve',
#             'objects': http.request.env['db_corn_retrieve.db_corn_retrieve'].search([]),
#         })

#     @http.route('/db_corn_retrieve/db_corn_retrieve/objects/<model("db_corn_retrieve.db_corn_retrieve"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('db_corn_retrieve.object', {
#             'object': obj
#         })