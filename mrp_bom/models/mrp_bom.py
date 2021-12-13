from odoo import fields, models


class MrpBom(models.Model):
    _inherit = 'mrp.production'

    def get_bom(self):
        return {
            # 'type': 'ir.actions.report',
            # 'name': 'BOM',
            # 'view_mode': '',
            # 'res_model': 'action_report_bom_structure',
            # 'domain': ['product_id', '=', self.product_id],
        }
