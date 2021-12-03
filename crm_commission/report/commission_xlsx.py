
import base64
import io
from odoo import models


class CommissionXlsx(models.Model):
    _name = 'report.crm_commission.report_commission_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, commissions):
        print('excel', data['commission'], )
        print(data['form_data'])

        # domain = []
        # if data.get('team_id'):
        #     domain.append(('id', 'in', data.get('team_id')))
        # print(domain)

        sheet = workbook.add_worksheet('Commission Plan')
        bold = workbook.add_format({'bold': True})
        format1 = workbook.add_format({'bold': True, 'color': '#COCOCO', 'align': 'center'})
        format2 = workbook.add_format({'bold': True, 'align': 'center'})
        # format1.ali
        sheet.set_column('A:A', 12)
        sheet.set_column('B:B', 10)
        sheet.set_column('C:C', 13)
        sheet.set_column('D:D', 12)
        sheet.set_column('E:E', 12)
        sheet.set_column('F:F', 12)

        sheet.merge_range('A1:D1', 'COMMISSION PLAN', format1)
        if data['form_data']['from_date']:
            sheet.write(1, 0, 'From Date:', format2)
            sheet.write(1, 1, data['form_data']['from_date'], format2)
        if data['form_data']['to_date']:
            sheet.write(1, 2, 'To Date:', format2)
            sheet.write(1, 3, data['form_data']['to_date'], format2)
        if len(data['team']) > 0:
            col = 0
            sheet.write(2, 0, 'Sales Team', format2)
            for rec in range(0, len(data['team'])):
                col = col+1
                sheet.write(2, col, data['team_name'][rec])
            # sheet.write(2, 0, 'Sales Team', format2)
            # for commission in data['commission']:
            #     team = commission['team_id'][1]
            # sheet.write(2, 1, team, format2)
        if len(data['salesperson']) > 0:
            col = 0
            sheet.write(3, 0, 'Salesperson', format2)
            for rec in range(0, len(data['salesperson'])):
                col = col + 1
                sheet.write(3, col, data['salesperson_name'][rec])

        # if len(data['salesperson']) == 1:
        #     sheet.write(2, 2, 'Salesperson', format2)
        #     for commission in data['commission']:
        #         user = commission['user_id'][1]
        #     sheet.write(2, 3, user, format2)

        # sheet.write()
        row = 4
        # sheet.write(row, 0, )
        col = 0
        if len(data['team']) > 1:
            # print('team')
            if len(data['salesperson']) > 1:
                # print('usr')
                sheet.write(row, col, 'Plan no', bold)
                sheet.write(row, col + 1, 'plan name', bold)
                sheet.write(row, col+2, 'sales person', bold)
                sheet.write(row, col+3, 'sales team', bold)
                sheet.write(row, col + 4, 'total revenue', bold)
                sheet.write(row, col + 5, 'commission amount', bold)
                for commission in data['commission']:
                    row = row + 1
                    sheet.write(row, col, commission['sequence'], )
                    sheet.write(row, col + 1, commission['name'], )
                    sheet.write(row, col + 2, commission['user_id'][1], )
                    sheet.write(row, col + 3, commission['team_id'][1], )
                    sheet.write(row, col + 4, commission['revenue'], )
                    sheet.write(row, col + 5, commission['total'], )
            else:
                sheet.write(row, col, 'Plan no', bold)
                sheet.write(row, col + 1, 'plan name', bold)
                # sheet.write(row, col + 2, 'sales person', bold)
                sheet.write(row, col + 2, 'sales team', bold)
                sheet.write(row, col + 3, 'total revenue', bold)
                sheet.write(row, col + 4, 'commission amount', bold)
                for commission in data['commission']:
                    row = row + 1
                    sheet.write(row, col, commission['sequence'], )
                    sheet.write(row, col + 1, commission['name'], )
                    # sheet.write(row, col + 2, commission['user_id'][1], )
                    sheet.write(row, col + 2, commission['team_id'][1], )
                    sheet.write(row, col + 3, commission['revenue'], )
                    sheet.write(row, col + 4, commission['total'], )
        else:
            if len(data['salesperson']) > 1:
                sheet.write(row, col, 'Plan no', bold)
                sheet.write(row, col + 1, 'plan name', bold)
                sheet.write(row, col + 2, 'sales person', bold)
                # sheet.write(row, col + 3, 'sales team', bold)
                sheet.write(row, col + 3, 'total revenue', bold)
                sheet.write(row, col + 4, 'commission amount', bold)
                for commission in data['commission']:
                    row = row + 1
                    sheet.write(row, col, commission['sequence'], )
                    sheet.write(row, col + 1, commission['name'], )
                    sheet.write(row, col + 2, commission['user_id'][1], )
                    # sheet.write(row, col + 3, commission['team_id'][1], )
                    sheet.write(row, col + 3, commission['revenue'], )
                    sheet.write(row, col + 3, commission['total'], )
            else:
                sheet.write(row, col, 'Plan no', bold)
                sheet.write(row, col + 1, 'plan name', bold)
                # sheet.write(row, col + 2, 'sales person', bold)
                # sheet.write(row, col + 3, 'sales team', bold)
                sheet.write(row, col + 2, 'total revenue', bold)
                sheet.write(row, col + 3, 'commission amount', bold)
                for commission in data['commission']:
                    row = row + 1
                    sheet.write(row, col, commission['sequence'], )
                    sheet.write(row, col + 1, commission['name'], )
                    # sheet.write(row, col + 2, commission['user_id'][1], )
                    # sheet.write(row, col + 3, commission['team_id'][1], )
                    sheet.write(row, col + 2, commission['revenue'], )
                    sheet.write(row, col + 3, commission['total'], )

        # sheet.write(row, col, 'Plan no', bold)
        # sheet.write(row, col+1, 'plan name', bold)
        # # sheet.write(row, col+2, 'sales person', bold)
        # # sheet.write(row, col+3, 'sales team', bold)
        # sheet.write(row, col+4, 'total revenue', bold)
        # sheet.write(row, col+5, 'commission amount', bold)
        #
        # for commission in data['commission']:
        #
        #     row = row + 1
        #
        #     sheet.write(row, col, commission['sequence'], )
        #     sheet.write(row, col + 1, commission['name'], )
        #     # sheet.write(row, col + 2, commission['user_id'][1], )
        #     # sheet.write(row, col + 3, commission['team_id'][1], )
        #     sheet.write(row, col + 4, commission['revenue'], )
        #     sheet.write(row, col + 5, commission['total'], )


