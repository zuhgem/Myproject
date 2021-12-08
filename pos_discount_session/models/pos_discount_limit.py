from odoo import fields, models, api


class DiscountLimit(models.Model):
    _inherit = 'pos.session'

    is_discount_limit = fields.Boolean(string='Discount limit'
                                       )
    discount_limit = fields.Float(string='Limit')
    discount_category_ids = fields.Many2many('pos.category',
                                             string='Categories')


class DiscountLimitCategory(models.Model):
    _inherit = 'pos.config'

    is_discount_limit = fields.Boolean(string="Discount Limit", required=True)
    discount_limit = fields.Integer(string='Limit', required=True)
    discount_categ_ids = fields.Many2many('pos.category', 'reference',
                                          required=True, string="Category")

