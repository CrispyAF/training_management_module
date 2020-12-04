# -*- coding: utf-8 -*-
# from odoo import http


# class BtManagement(http.Controller):
#     @http.route('/bt_management/bt_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bt_management/bt_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bt_management.listing', {
#             'root': '/bt_management/bt_management',
#             'objects': http.request.env['bt_management.bt_management'].search([]),
#         })

#     @http.route('/bt_management/bt_management/objects/<model("bt_management.bt_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bt_management.object', {
#             'object': obj
#         })
