# -*- coding: utf-8 -*-
# from odoo import http


# class EfsDemo001(http.Controller):
#     @http.route('/efs_demo_001/efs_demo_001', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/efs_demo_001/efs_demo_001/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('efs_demo_001.listing', {
#             'root': '/efs_demo_001/efs_demo_001',
#             'objects': http.request.env['efs_demo_001.efs_demo_001'].search([]),
#         })

#     @http.route('/efs_demo_001/efs_demo_001/objects/<model("efs_demo_001.efs_demo_001"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('efs_demo_001.object', {
#             'object': obj
#         })

