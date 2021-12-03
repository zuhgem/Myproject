import io
import json

from odoo import models, fields
from odoo.http import request
from odoo.tools import date_utils

try:
    from odoo.tools.misc import xlsxwriter
except ImportError:
    import xlsxwriter


class ReportButton(models.TransientModel):
    _name = 'commission_wizard'

    from_date = fields.Date('From Date')
    to_date = fields.Date('To date')
    team_ids = fields.Many2many('crm.team', string='Sales Team', )
    user_ids = fields.Many2many('res.users', string='Salesperson',
                              domain=lambda self: [('groups_id', 'in',
                            self.env.ref('sales_team.group_sale_salesman').id)])

    def action_report_pdf(self):
        print('pdf', self.read()[0])
        domain = []
        salesperson = []
        salesperson_name = []
        team = []
        team_name = []
        for rec in self.user_ids:
            salesperson.append(rec.id)
            salesperson_name.append(rec.name)
        print(salesperson_name)
        for rec in self.team_ids:
            team.append(rec.id)
            team_name.append(rec.name)
        if self.user_ids:
            if self.team_ids:
                domain.append(('team_id', 'in', team))
                domain.append(('user_id', 'in', salesperson))
                # domain = [('team_id', 'in', team),
                #           ('user_id', 'in', salesperson)]
            else:
                domain.append(('user_id', 'in', salesperson))
                # domain = [('user_id', 'in', salesperson)]
        else:
            if self.team_ids:
                domain.append(('team_id', 'in', team))

                # domain = [('team_id', 'in', team)]
            else:
                domain = [('sequence', '!=', 'New')]
        if self.from_date:
            domain.append(('from_date', '>=', self.from_date))
        if self.to_date:
            domain.append(('to_date', '<=', self.to_date))
        print(salesperson, team_name)
        commission = self.env['crm.commission'].search_read(domain)
        data = {
            'form_data': self.read()[0],
            'commission': commission,
            'salesperson': salesperson,
            'team': team,
            'salesperson_name': salesperson_name,
            'team_name': team_name
        }
        return self.env.ref('crm_commission.action_report_commission_pdf').\
            report_action(self, data=data)

    def action_report(self):
        print('report')
        domain = []
        # if self.from_date:
        #     domain += [('from_date', '>=', self.from_date)]
        # if self.to_date:
        #     domain += [('to_date', '>=', self.to_date)]
        # if self.team_ids:
        #     for rec in self:
        #         domain.append(('team_id', '=', rec.team_ids.id))
        # for rec in self:
        #     for record in rec:
        #         if record.team_ids:
        #             list_ = list(record.team_ids)
        #             print(list_)
        #             num = 1
        #             domain.append(('team_id', '=', list(record.team_ids)[num].id))
        domain_ =[]
        salesperson = []
        salesperson_name = []
        team = []
        team_name = []
        for rec in self.user_ids:
            salesperson.append(rec.id)
            salesperson_name.append(rec.name)
        print(salesperson_name)
        for rec in self.team_ids:
            team.append(rec.id)
            team_name.append(rec.name)
        print(salesperson, team_name)
        if self.user_ids:
            if self.team_ids:
                domain.append(('team_id', 'in', team))
                domain.append(('user_id', 'in', salesperson))
                # domain = [('team_id', 'in', team),
                #           ('user_id', 'in', salesperson)]
            else:
                domain.append(('user_id', 'in', salesperson))
                # domain = [('user_id', 'in', salesperson)]
        else:
            if self.team_ids:
                domain.append(('team_id', 'in', team))

                # domain = [('team_id', 'in', team)]
            else:
                domain = [('sequence', '!=', 'New')]


        # for rec in self:
        #     users_selected = []
        #     team_selected = []
        #     if rec.team_ids:
        #         # domain.append('|')
        #         for i in range(len(rec.team_ids)):
        #             # team_selected.append(list(rec.team_ids)[i].name)
        #             domain.append(('team_id', '=', list(rec.team_ids)[i].name))
        #             # domain.append('|')
        #         # domain.append(('team_id', 'in', team_selected))
        #     if rec.user_ids:
        #         for i in range(len(rec.user_ids)):
        #             # users_selected.append(rec.user_ids.id)
        #             domain.append(('user_id', '=', list(rec.user_ids)[i].id))
        #             # domain.append('|')
        #     # domain.append(('team_id', 'in', users_selected))
        if self.from_date:
            domain.append(('from_date', '>=', self.from_date))
        if self.to_date:
            domain.append(('to_date', '<=', self.to_date))

        print(domain)
        commission = self.env['crm.commission'].search_read(domain)
        data = {
            'commission': commission,
            'form_data': self.read()[0],
            'salesperson': salesperson,
            'team': team,
            'salesperson_name': salesperson_name,
            'team_name': team_name
        }
        return self.env.ref('crm_commission.report_commission_xlsx').\
            report_action(self, data=data)
    #     active_record = self._context['active_id']
    #     print(active_record)
    #     record = self.env['crm.commission'].browse(active_record)
    #     print(record)
    #     data = {
    #         'ids': self.ids,
    #         'model': self._name,
    #         'record': record.id
    #     }
    #     print(data)
    #     return {
    #         'type': 'ir.actions.report',
    #         'data': {
    #             'model': 'commission_wizard',
    #             'options': json.dumps(data, default=date_utils.json_default),
    #             'output_format': 'xlsx',
    #             'report_name': 'commission report'
    #         },
    #         'report_type': 'xlsx'
    #     }
    #
    # def get_xlsx_report(self, data, response):
    #     output = io.BytesIO()
    #     workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    #     name = data['record']
    #     user_obj = self.env.user
    #     wizard_record = request.env['commission_wizard'].search([])[-1]
    #     task_obj = request.env['crm.commission']
    #     users_selected = []
    #     team_selected = []
    #     for elements in wizard_record.user_ids:
    #         users_selected.append(elements.id)
    #     for elements in wizard_record.team_ids:
    #         team_selected.append(elements.id)
    #     if wizard_record.user_ids:
    #         if wizard_record.team_ids:
    #             current_commission = task_obj.search([
    #                 ('name', '=', name),
    #                 ('team_id', 'in', team_selected),
    #                 ('user_id', 'in', users_selected)])
    #         else:
    #             current_commission = task_obj.search([
    #                 ('name', '=', name),
    #                 ('user_id', 'in', users_selected)])
    #     else:
    #         if wizard_record.team_ids:
    #             current_commission = task_obj.search([
    #                 ('name', '=', name),
    #                 ('team_id', 'in', team_selected)])
    #         else:
    #             current_commission = task_obj.search([
    #                 ('name', '=', name)])
    #     vals = []
    #     for commission in current_commission:
    #         vals.append({
    #             'name': commission.name,
    #             'user_id': commission.user_id,
    #             'team_id': commission.team_id
    #         })
    #
    #     sheet = workbook.add_worksheet("commission Report")
    #     format1 = workbook.add_format({'font_size': 22, 'bg_color': '#D3D3D3'})
    #     format2 = workbook.add_format({'font_size': 12, 'bold': True, 'bg_color': '#FFFFFF'})
    #     format3 = workbook.add_format({'font_size': 10})
    #     format4 = workbook.add_format({'font_size': 22})
    #     format5 = workbook.add_format({'font_size': 10, 'bg_color': '#FFFFFF'})
    #     format6 = workbook.add_format({'font_size': 10, 'bg_color': '#FFFFFF'})
    #
    #     format6.set_align('center')
    #
    #     sheet.merge_range('A1:B1', user_obj.company_id.name, format5)
    #     sheet.merge_range('A2:B2', user_obj.company_id.street, format5)
    #     sheet.write('A3', user_obj.company_id.city, format5)
    #     sheet.write('B3', user_obj.company_id.zip, format5)
    #     sheet.merge_range('A4:B4', user_obj.company_id.state_id.name, format5)
    #     sheet.merge_range('A5:B5', user_obj.company_id.country_id.name, format5)
    #
    #     sheet.merge_range('C5:H5', "", format1)
    #
    #     workbook.close()
    #     output.seek()
    #     response.stream.write(output.read())


