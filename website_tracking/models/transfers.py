from odoo import models, fields


class Transfer(models.Model):
    _inherit = 'stock.picking'

    transfer_ids = fields.One2many('transfer', 'transfer_id', string='Transfer')


class TransferTable(models.Model):
    _name = 'transfer'

    to_ = fields.Char('To')
    from_ = fields.Char('From')
    date = fields.Date('Date')
    transfer_id = fields.Many2one('stock.picking')
