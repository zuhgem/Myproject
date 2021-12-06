odoo.define('pos_product_rating.receipt', function(require){
    "use strict";
    var models = require('point_of_sale.models');
    models.load_fields('product.product', 'rating');
    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function(){
            var line = _super_orderline.export_for_printing.apply(this, arguments);
            line.rating = this.get_product().rating;
            return line;
        }
    });
});