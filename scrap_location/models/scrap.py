from odoo import models, fields, api


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    loc = fields.Many2one('stock.location', ' Location',)

    # def _get_default_scrap_location_id(self):
    #     # print('scrap')
    #     return super(StockScrap, self)._get_default_scrap_location_id()

    @api.onchange('product_id')
    def _onchange_product_id(self):
        print(self.product_id.name)
        if self.product_id:
            search = self.env['stock.putaway.rule'].search([('product_id', '=', self.product_id.id)])
            if search:
                print('True')
                self.location_id = search.location_out_id
                self.product_uom_id = self.product_id.uom_id
            else:
                print("False")

