import xlrd

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class Import(models.TransientModel):
    _name = 'import_wizard'

    file_path = fields.Char('File path')

    # res_model = fields.Char('Related Document Model', required=True)
    # res_id = fields.Integer('Related Document ID', required=False)
    # name = fields.Char()


    def action_import(self):
        # print('Import')
        # path = self.file_path
        # print(path)
        # workbook = xlrd.open_workbook(path)
        # sheet = workbook.sheet_by_index(0)
        # print(sheet.ncols)
        active_id = self.env.context.get('active_id')
        # print(active_id)
        search = self.env['sale.order'].browse(active_id)
        try:
            book = xlrd.open_workbook(filename=self.file_path)
            print(book)
        except FileNotFoundError:
            raise UserError(
                'No such file or directory found. \n%s.' % self.file_name)
        except xlrd.biffh.XLRDError:
            raise UserError('Only excel files are supported.')
        for sheet in book.sheets():
            try:
                line_vals = []
                if sheet.name == 'Sheet1':
                    for row in range(sheet.nrows):
                        if row >= 1:
                            row_values = sheet.row_values(row)
                            # print(row_values)
                            vals = self._create_order_lines(row_values)
                            # print(vals)
                            line_vals.append((0, 0, vals))
                            print(line_vals)
                if line_vals:
                    search.update({
                        'order_line': line_vals
                    })
            except IndexError:
                pass

    def _create_order_lines(self, record):
        name = record[0]
        product_id = self.env['product.product'].search([('name', '=', name)],
                                                        limit=1)
        if not product_id:
            raise UserError(_("There is no product with code %s.") % name)
        uom = record[4]
        product_uom = self.env['uom.uom'].search([('name', '=', uom)], limit=1)
        if not product_uom:
            raise UserError(_("There is no uom with name %s.") % uom)
        line_ids = {
            'product_id': product_id.id,
            'name': record[2],
            'product_uom_qty': float(record[1]),
            'price_unit': record[3],
            'product_uom': product_uom.id
        }
        return line_ids