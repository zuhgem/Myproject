{
    'name': 'website Snippets',
    'summary': 'most viewed and most sold products',
    'version': '1.0',
    'description': "",
    'depends': ['website', 'website_sale'],
    'qweb': [],
    'data': [
        'views/snippets.xml',
        'views/sold_products.xml',
        'views/viewed_product.xml',
        'views/snippet_view.xml',
    ],
    'installable': True,
    'application': True,
}
