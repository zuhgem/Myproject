odoo.define('pos_discount_limit', function(require){
    "use strict";
    var models = require('point_of_sale.models');
    var field_utils = require('web.field_utils');
    var config = require('web.config');
    models.load_fields('pos.config', 'discount_limit');
    models.load_fields('pos.config', 'discount_categ_ids');
    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
            set_discount: function(discount) {
                var discount_category = this.pos.config.discount_categ_ids
                var category = this.get_product().pos_categ_id[0]
                var flag = false
                for (var categ in discount_category){
                    if (category == discount_category[categ]){
                        flag = true
                    }
                }
                if (flag == true){
                    var parsed_discount = isNaN(parseFloat(discount)) ? 0 : field_utils.parse.float('' + discount);
                    var disc = Math.min(Math.max(parsed_discount || 0, 0),100);
                    this.discount = disc;
                    this.discountStr = '' + disc;
                    if (this.discountStr < this.pos.config.discount_limit){
                       this.trigger('change',this);
                    }
                    else{
                        alert("Discount Limit Exceeded")
                    }
                }
                else{
                    var parsed_discount = isNaN(parseFloat(discount)) ? 0 : field_utils.parse.float('' + discount);
                    var disc = Math.min(Math.max(parsed_discount || 0, 0),100);
                    this.discount = disc;
                    this.discountStr = '' + disc;
                    this.trigger('change',this);
//                    flag = true
                }
            }


        });

});