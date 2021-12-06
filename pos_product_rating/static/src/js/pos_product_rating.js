odoo.define('pos_product_rating.rating', function(require) {
"use strict";
var models = require('point_of_sale.models');
var _super_product = models.PosModel.prototype;
var _super_orderline = models.Orderline.prototype;
models.load_fields('product.product', 'rating');
models.PosModel = models.PosModel.extend({
//console.log('sdas')
    initialize: function(session, attributes) {
        models.load_fields('product.product', 'rating');
        _super_product.initialize.apply(this, arguments);
        }
    });
models.Orderline = models.Orderline.extend({
    initialize: function(attrs, options){
        var line = _super_orderline.initialize.apply(this, arguments);
        this.rating = this.product.rating;
        }
    });
});