from odoo import http
from odoo.http import request


class CustomSnippets(http.Controller):

    @http.route(['/website_snippets/product'], type='json', auth="public", website=True)
    def sold(self):
        # products_ = request.website.get_product()
        products = request.env['product.product'].search([('is_published', '=', 'True')])
        # print(sorted(products))
        # print(products)
        sort_pro = sorted(products)
        # print(sort_pro)
        length = len(sort_pro)
        for rec in range(length-1):
            for record in range(0, length - rec - 1):
                if sort_pro[record].sales_count < sort_pro[record + 1].sales_count:
                    sort_pro[record], sort_pro[record + 1] = sort_pro[record + 1], sort_pro[record]
        # print(sort_pro)
        data = []
        for product in sort_pro:
            if len(data) < 5:
                fields = product.read(
                    ['display_name', 'description_sale', 'list_price',
                     'website_url'])[0]
                fields['image'] = request.env['website'].image_url(product,
                                                                   'image_512')
                data.append(fields)
        return request.env['ir.ui.view']._render_template\
            ('website_snippets.products_card', {'products': data})

    @http.route(['/website_snippets/view_products'], type='json', auth="public", website=True)
    def view(self):
        products = request.env['product.product'].search(
            [('is_published', '=', 'True')])
        # print(sorted(products))
        # print(products)
        sort_pro = sorted(products)
        # print(sort_pro)
        length = len(sort_pro)
        for rec in range(length - 1):
            for record in range(0, length - rec - 1):
                if sort_pro[record].view_count < sort_pro[record + 1].view_count:
                    sort_pro[record], sort_pro[record + 1] = sort_pro[record + 1], sort_pro[record]
        # print(sort_pro)
        data_ = []
        for product in sort_pro:
            if len(data_) < 5:
                fields = product.read(
                    ['display_name', 'description_sale', 'list_price',
                     'website_url'])[0]
                fields['image'] = request.env['website'].image_url(product,
                                                                   'image_512')
                data_.append(fields)
        # products = request.env['product.product'].search([])
        # views = request.env['website.track'].search([])
        # data_ = []
        # viewed_product = []
        # for product in products:
        #     for view in views:
        #         if view.product_id == product:
        #             # print('Equal')
        #             viewed_product.append(product)
        # print(viewed_product)
        # for product in viewed_product:
        #     print(('view.......', product.view_count))
        #     fields = product.read(['display_name', 'description_sale', 'list_price',
        #                  'website_url'])[0]
        #     fields['image'] = request.env['website'].image_url(product,
        #                                                                'image_512')
        #     data_.append(fields)
        return request.env['ir.ui.view']._render_template('website_snippets.view_products_card', {'products_': data_})
