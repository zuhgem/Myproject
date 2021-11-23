{
    'name': 'sale order from pos',
    'version': '14.0.0.1',

    'summary': 'Link module between Point of Sale and Sales',
    'description': """
""",
    'depends': ['point_of_sale', 'sale_management'],
    'data': ['security/ir.model.access.csv',
             'views/sale_pos.xml',
             'wizard/payment.xml'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}