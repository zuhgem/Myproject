from odoo import http
from odoo.http import request


class Tracking(http.Controller):

    @http.route('/tracking', auth='public', website=True)
    def index(self):
        return request.render('website_tracking.tracking_page')

    @http.route('/tracked', auth='public', website=True)
    def Tracked(self, **kw):
        print('asdf', kw)
        web = request.env['website'].get_current_website()
        print('web', web)
        user = request.env.user
        print('user', user.name)
        domain = []
        domain.append(('website_id', '=', web.name))
        domain.append(('partner_id.name', '=', user.name))
        domain.append(('date_order', '>=', kw['from_date']))
        domain.append(('date_order', '<=', kw['to_date']))
        order = request.env['sale.order'].search(domain)
        # order = http.request.env['sale.order'].sudo().search([])
        print('order', order)

        return request.render('website_tracking.tracking_done', {'order': order})