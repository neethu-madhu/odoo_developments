odoo.define('pos_discount_tag.pos_discount_tag', function(require){
    'use strict';

    var models = require('point_of_sale.models');
    const ProductScreen = require('point_of_sale.ProductScreen');
    models.load_fields('product.product', ['discount_tag']);

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        initialize: function(attr,options){
            _super_orderline.initialize.apply(this, arguments);
            if (options.json) {
                try {
                    this.init_from_JSON(options.json);
                } catch(error) {
                    console.error('ERROR: attempting to recover product ID', options.json.product_id,
                        'not available in the point of sale. Correct the product or clean the browser cache.');
                }
                return;
            }
            this.product = options.product;
            if(this.product.discount_tag){
                this.discount = this.product.discount_tag;
            }
            else{
               this.discount = 0;
            }

        },
    });
});
