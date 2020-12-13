# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import TableCompute


class BrandFilter(http.Controller):
    @http.route(['/shop/brand/<model("product.brand"):brand>'],
                type='http', auth="public", website=True)
    def brandProduct(self, brand=None, page=0, search='', ppg=False, **post):
        Brand = request.env['product.brand']
        if brand:
            brand = Brand.search([('id', '=', int(brand))], limit=1)
        else:
            brand = Brand
        if brand:
            url = "/shop/brand/%s" % slug(brand)
        # filtering of the products
        product_obj = request.env['product.template']
        Product = product_obj.sudo().search([('website_published', '=', True),
                                             ('brand_id', '=', brand.id)])
        if ppg:
            try:
                ppg = int(ppg)
                post['ppg'] = ppg
            except ValueError:
                ppg = False
        if not ppg:
            ppg = request.env['website'].get_current_website().shop_ppg or 20

        ppr = request.env['website'].get_current_website().shop_ppr or 4
        pager = request.website.pager(
            url=url,
            total=len(Product),
            page=page,
            step=ppg
        )
        products = product_obj.sudo().search([('brand_id', '=', brand.id),
                                              ('website_published', '=', True)],
                                             order="id desc", offset=pager['offset'])
        keep = QueryURL('shop/brand')
        values = {
            'pager': pager,
            'products': products,
            'bins': TableCompute().process(products, ppg, ppr),
            'rows': ppr,
            'keep': keep,
        }
        return request.render("website_sale.products", values)
