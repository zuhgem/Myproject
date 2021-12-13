
from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class ProductProduct(models.Model):
    _inherit = 'product.product'

    view_count = fields.Float(compute='_compute_view_count', string='View')

    def _compute_view_count(self):
        r = {}
        # self.view_count = 0
        for rec in self:
            count = self.env['website.track'].search_count([('product_id', '=', rec.id)])
            rec.view_count = count




