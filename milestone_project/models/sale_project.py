from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    milestone = fields.Integer(string="Milestone")


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_create_project(self):
        self.ensure_one()
        print('project')
        search = self.env['project.project'].search([('name', '=', self.name)])
        if search:
            print('search')
        else:
            project = self.env['project.project'].create({
                'name': self.name,
                'partner_id': self.partner_id.id,
                'user_id': self.user_id.id,
            })
            for record in self:
                for rec in record.order_line:
                    print(rec.milestone)
                    if rec.milestone:
                        # name = 'Milestone ' + str(rec.milestone)
                        # for rec1 in record.order_line:
                        #     name1 = 'Milestone ' + str(rec.milestone)
                        #     if name == name1:
                        #         print('same')
                        name = 'Milestone ' + str(rec.milestone)
                        task_search = self.env['project.task'].search([('name', '=', name), ('project_id', '=', self.name)])
                        print(task_search)
                        if task_search:
                            print("task")
                            sub = rec.env['project.task'].create({
                                'name': task_search.name + ' - ' + rec.product_id.name,
                                'project_id': self.env['project.project'].search([('name', '=', self.name)]).id,
                                'parent_id': task_search.id
                            })
                        else:
                            task = rec.env['project.task'].create({
                                'name': name,
                                'project_id': self.env['project.project'].search([('name', '=', self.name)]).id
                            })
                            sub = rec.env['project.task'].create({
                                'name': task.name + ' - ' + rec.product_id.name,
                                'project_id': self.env['project.project'].search([('name', '=', self.name)]).id,
                                'parent_id': task.id
                            })
                    else:
                        task = record.env['project.task'].create({
                            'name': rec.product_id.name,
                            'project_id': self.env['project.project'].search([('name', '=', self.name)]).id
                        })

                    # for rec_1 in record.order_line:
                    #     print(rec_1.milestone)
                    #     name_2 = 'Milestone ' + str(rec.milestone)
                    #     if name == name_2:
                    #         print('same')
                    #         name = 'Milestone ' + str(rec.milestone)
                    #         search_task = self.env['project.task'].search([('name', '=', name)])
                    #         if search_task:
                    #             print(name)
                    #         # else:
                    #         task = rec.env['project.task'].create({
                    #             'name': name,
                    #             'project_id': self.env['project.project'].search([('name', '=', self.name)]).id
                    #         })
                    #     sub = rec.env['project.task'].create({
                    #         'name': task.name + ' - ' + rec.product_id.name,
                    #         'project_id': self.env['project.project'].search([('name', '=', self.name)]).id,
                    #         'parent_id': task.id
                    #     })

        # if self.order_line:
        #     print("order line")
        #     for rec in self.order_line:
        #         if rec.milestone:
        #             name = 'Milestone' + str(rec.milestone)
        #             task = rec.env['project.task'].create({
        #                 'name': name,
        #                 'project_id': self.env['project.project'].search([('name', '=', self.name)]).id
        #             })
        #         task = rec.env['project.task'].create({
        #             'name': rec.product_id.name,
        #             'project_id': self.env['project.project'].search([('name', '=', self.name)]).id
        #         })
        #     if self.order_line.milestone:
        #         print('mile')

