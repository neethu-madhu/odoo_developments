# -*- coding: utf-8 -*-

from odoo import models, fields


class DiscountPrizeTag(models.Model):
    _inherit = 'product.template'
    # defines new field
    discount_tag = fields.Integer(string="Discount Price Tag")
