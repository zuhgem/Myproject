from odoo import fields, models, api


class Commission(models.Model):
    _name = 'crm.commission'
    _rec_name = 'sequence'

    sequence = fields.Char(string="Sequence", default='New', required=True,
                           readonly=True, copy=False)
    name = fields.Char(string='name')
    active = fields.Boolean('Active', default=True)
    from_date = fields.Date('From date')
    to_date = fields.Date('To date')
    type = fields.Selection([('product', 'Product Wise'),
                             ('revenue', 'Revenue Wise')], string='Type')
    from_amount = fields.Float("From Amount")
    to_amount = fields.Float("To Amount")
    team_id = fields.Many2one('crm.team', 'Sales Team',)
    user_id = fields.Many2one('res.users', string='Salesperson',
                              domain=lambda self: [('groups_id', 'in',
                        self.env.ref('sales_team.group_sale_salesman').id)])

    line_ids = fields.One2many('product.lines', 'line_id')
    total = fields.Float('Total', compute='_compute_total', store=True)
    revenue = fields.Float('Revenue', compute='_compute_total', store=True)

    total_sold = fields.Float('sold')
    commission = fields.Float('Commission %')

    @api.model
    def create(self, vals_list):
        if vals_list.get('sequence', 'New') == 'New':
            vals_list['sequence'] = self.env['ir.sequence'].next_by_code(
                'self.commission') or 'New'
        res = super(Commission, self).create(vals_list)
        return res

    @api.depends('line_ids.commission', 'commission', 'total_sold')
    def _compute_total(self):
        for rec in self:
            if rec.type == 'product':
                for order in rec:
                    total = 0.00
                    revenue = 0.00
                    for line in order.line_ids:
                        total = total + line.sub
                        revenue = revenue + line.rate
                    order.update({
                        'total': total,
                        'revenue': revenue + total
                    })
            elif rec.type == 'revenue':
                rec.total = rec.total_sold * rec.commission / 100
                rec.revenue = rec.total + rec.total_sold


class Product(models.Model):
    _name = 'product.lines'

    product_id = fields.Many2one('product.product', string='Product')
    categ_id = fields.Many2one('product.category', 'Product Category', )

    rate = fields.Float('Rate')
    commission = fields.Float('Commission Amount %')
    sub = fields.Float('sub', compute='_compute_sub', store=True)

    line_id = fields.Many2one('crm.commission')

    @api.onchange('product_id')
    def onchange_rate(self):
        if self.product_id:
            self.rate = self.product_id.lst_price
            self.categ_id = self.product_id.categ_id

    @api.depends('rate', 'commission')
    def _compute_sub(self):
        for rec in self:
            if rec.rate and rec.commission:
                rec.sub = rec.rate * rec.commission/100