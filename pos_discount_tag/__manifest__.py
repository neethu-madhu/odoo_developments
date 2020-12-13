# -*- coding: utf-8 -*-
{
    'name': "POS Discount Tag",

    'summary': """POS Product Discount Management""",

    'description': """POS Product Discount Management""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'category': 'Sales/Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/discount_price_tag.xml',
    ],
}
