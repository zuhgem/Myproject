from odoo import models, fields, api


class PosOrder(models.Model):
    _inherit = 'pos.order'

    ref = fields.Char('Reference')

    def data_in_order_line(self, line):
        return {
            'product_id': line.product_id.id,
            'product_uom_qty': line.qty,
            'price_unit': line.product_id.list_price,
            'name': 'asdsaf',
            'customer_lead': 0.00,
            # 'qty_delivered_method': 'manual',
            # 'qty_delivered': 0.00,
            # 'qty_invoiced': 0.00,
            'product_uom': line.product_uom_id.id
        }

    def fields_order_line(self):
        order_lines = [(6, 0, 0)]
        for line in self.lines:
            data = self.data_in_order_line(line)
            order_lines.append((0, 0, data))
        # data = self.data_in_order_line()
        return order_lines

    # @api.model
    # def default_get(self, fields_list):
    #     res = super(PosOrder, self).default_get(fields_list)
    #     res_id = self._context.get('active_id')
    #     res_model = self._context.get('active_model')
    #     res.update({'res_id': res_id, 'res_model': res_model})
    #     if res_id and res_model == 'pod.order':
    #         record = self.env[res_model].browse(res_id)
    #         res.update({
    #             'partner_id': self.partner_id.id,
    #         })
    #     return res

    def action_sale_order(self):
        self.ensure_one()
        lines = self.fields_order_line()
        print(lines)
        print('sale order')
        sale_order = self.env['sale.order'].create({
            'partner_id': self.partner_id.id,
            'state': 'sale',
            'order_line': lines,
            # 'order_line': [ (0, 0, {
            #     'product_id': self.lines.product_id.id,
            #     'product_uom_qty': 1.0,
            #     'price_unit': 23.0,
            #     'name': 'asd',
            #     'qty_delivered': 0.00,
            #     'qty_invoiced': 0.00,
            #     'qty_delivered_method': 'manual'
            # })]
        })



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pos_session = fields.Many2one('pos.session', string='Pos Session')
    state = fields.Selection(selection_add=[('Paid', 'paid at the counter'), ('cancel',)])
    boolean = fields.Selection([('draft', 'Draft'), ('post', 'Post')])
    paid_state = fields.Integer(default=1)

    def compute_data(self, line):
        name = '[' + line.product_id.default_code + ']' + line.product_id.name
        return {
            "full_product_name": name,
            'product_id': line.product_id.id,
            'qty': line.product_uom_qty,
            'price_unit': line.price_unit,
            'discount': 0.00,
            'product_uom_id': line.product_uom,
            'price_subtotal': line.price_subtotal,
            'price_subtotal_incl': line.price_subtotal,
            # 'tax_ids': line.tax_id
        }

    def data_line(self):
        order_lines = [(6, 0, 0)]
        for line in self.order_line:
            data = self.compute_data(line)
            order_lines.append((0, 0, data))
        return order_lines

    def action_pos(self):
        data_line = self.data_line()
        for rec in self:
            rec.write({'state': 'Paid'})
        search = self.env['pos.order'].search([('ref', '=', self.name)])
        if search:
            if search.state == 'paid':
                print('asd')
                self.boolean = 'post'
            else:
                print('lkj')
        else:
            session = self.env['pos.order'].create({
                # 'sale_order': self.name,
                'session_id': self.pos_session.id,
                'amount_tax': '',
                'amount_total': self.amount_total,
                'amount_paid': 0.00,
                'amount_return': 0.00,
                'partner_id': self.partner_id.id,
                'ref': self.name,
                'lines': data_line

            })
        # session = self.env['pos.order'].create({
        #     # 'sale_order': self.name,
        #     'session_id': self.pos_session.id,
        #     'amount_tax': '',
        #     'amount_total': self.amount_total,
        #     'amount_paid': 0.00,
        #     'amount_return': 0.00,
        #     'partner_id': self.partner_id.id,
        #     'ref': self.name,
        #     'lines': data_line
        #
        #     })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'payment_pos_wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'views': [(False, 'form')],
            'target': 'new',
        }
