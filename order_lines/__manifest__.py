{
    'name': 'Import Order lines',
    'version': '14.0.0.1',

    'summary': '',
    'description': """
""",
    'depends': ['sale_management'],
    'data': ['views/sales.xml',
             'security/ir.model.access.csv',
             'wizard/import_data.xml'],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}