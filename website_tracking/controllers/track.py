from odoo import http
from odoo.http import request


class TrackingOrder(http.Controller):

    @http.route('/tracking-order', auth='public', website=True)
    def index(self):
        return request.render('website_tracking.tracking_order')

    @http.route('/tracked-order', auth='public', website=True)
    def Tracked(self, **kw):
        print('asdf', kw)
        domain = []
        domain.append(('origin', '=', kw['order']))
        transfer = request.env['stock.picking'].search(domain)
        print('transfer', transfer['transfer_ids'])
        transfer_data = transfer['transfer_ids']
        return request.render('website_tracking.track_done',
                              {'transfer': transfer_data})