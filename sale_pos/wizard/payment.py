from odoo import fields, models, api


class Payment(models.TransientModel):
    _name = 'payment_pos_wizard'

    payment_method_id = fields.Many2one('pos.payment.method', string='Payment Method')
    amount = fields.Float(string='Total Amount')
    paid = fields.Float(string='Paid Amount')
    remaining = fields.Float('Remaining Amount', compute='compute_remaining', store=True)

    res_model = fields.Char('Related Document Model', required=True)
    res_id = fields.Integer('Related Document ID', required=False)
    name = fields.Char('name')
    session_id = fields.Many2one('pos.session')
    amount_tax = fields.Float(string='Taxes')
    amount_total = fields.Float(string='Total')
    partner_id = fields.Many2one('res.partner', string='Customer')
    company_id = fields.Many2one('res.company')

    product_id = fields.Many2one('product.product', string='Product')

    @api.depends('amount', 'paid')
    def compute_remaining(self):
        if self.amount:
            self.remaining = (self.amount - self.paid)
        pos = self.env['pos.order'].search([('ref', '=', self.name)])

    @api.model
    def default_get(self, fields_list):
        res = super(Payment, self).default_get(fields_list)
        res_id = self._context.get('active_id')
        res_model = self._context.get('active_model')
        res.update({'res_id': res_id, 'res_model': res_model})
        if res_id and res_model == 'sale.order':
            record = self.env[res_model].browse(res_id)

            res.update({
                'amount': record.amount_total,
                'name': record.name,
                # # # 'test_id': record.name,
                'session_id': record.pos_session.id,
                'amount_tax': record.amount_total,
                'amount_total': record.amount_total,
                'partner_id': record.partner_id.id,
                'company_id': record.company_id.id,
                'product_id' : record.order_line.product_id.id
                # 'lines': record.order_line
            })
        return res

    def action_payment(self):
        pos = self.env['pos.order'].search([('ref', '=', self.name)])
        sale = self.env['sale.order'].search([('name', '=', self.name)])
        if pos:
            print('order')
            # pos.update({
            #     'payment_ids': (0, 0, {
            #         'amount': self.paid,
            #         'payment_method_id': self.payment_method_id
            #     })
            # })
            pos.update({
                'amount_paid': self.paid,
            })
            if pos.state == 'paid':
                print(123)
            else:
                print(456)
        return