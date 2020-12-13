# -*- coding: utf-8 -*-
# from odoo import http


# class PosDiscountTag(http.Controller):
#     @http.route('/pos_discount_tag/pos_discount_tag/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_discount_tag/pos_discount_tag/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_discount_tag.listing', {
#             'root': '/pos_discount_tag/pos_discount_tag',
#             'objects': http.request.env['pos_discount_tag.pos_discount_tag'].search([]),
#         })

#     @http.route('/pos_discount_tag/pos_discount_tag/objects/<model("pos_discount_tag.pos_discount_tag"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_discount_tag.object', {
#             'object': obj
#         })
