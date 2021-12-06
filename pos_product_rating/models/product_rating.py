from odoo import fields, models


class ProductRating(models.Model):
    _inherit = 'product.template'

    rating = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'),
        ('4', '4'), ('5', '5')
    ], string='Rating')